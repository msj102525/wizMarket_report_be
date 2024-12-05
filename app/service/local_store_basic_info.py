import ssl
from fastapi import HTTPException
import logging
import os
from datetime import datetime, timezone, timedelta
import pytz
import requests


from app.crud.local_store_basic_info import (
    select_local_store_info_redux_by_store_business_number as crud_select_local_store_info_redux_by_store_business_number,
    select_local_store_info_by_store_business_number as crud_select_local_store_info_by_store_business_number,
    select_store_coordinate_by_store_business_number as crud_select_store_coordinate_by_store_business_number,
)
from app.schemas.report import (
    AqiInfo,
    LocalStoreBasicInfo,
    LocalStoreCoordinate,
    LocalStoreRedux,
    TLSAdapter,
    WeatherInfo,
)

logger = logging.getLogger(__name__)


def select_local_store_info_redux_by_store_business_number(
    store_business_id: str,
) -> LocalStoreRedux:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_local_store_info_redux_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreRedux Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Service LocalStoreRedux Error: {str(e)}"
        )


def select_local_store_info_by_store_business_number(
    store_business_id: str,
) -> LocalStoreBasicInfo:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_local_store_info_by_store_business_number(store_business_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreBasicInfo Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Service LocalStoreBasicInfo Error: {str(e)}"
        )


def get_weather_info_by_lat_lng(
    lat: float, lng: float, lang: str = "kr"
) -> WeatherInfo:
    try:
        apikey = os.getenv("OPENWEATHERMAP_API_KEY")
        if not apikey:
            raise HTTPException(
                status_code=500,
                detail="Weather API key not found in environment variables.",
            )

        api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={apikey}&lang={lang}&units=metric"

        # logger.info(f"Requesting weather data for lat={lat}, lng={lng}")
        weather_response = requests.get(api_url)
        weather_data = weather_response.json()

        if weather_response.status_code != 200:
            error_msg = (
                f"Weather API Error: {weather_data.get('message', 'Unknown error')}"
            )
            logger.error(error_msg)
            raise HTTPException(
                status_code=weather_response.status_code, detail=error_msg
            )

        # logger.info(f"Weather API response: {weather_data}")

        sunrise_timestamp = weather_data["sys"]["sunrise"]
        sunset_timestamp = weather_data["sys"]["sunset"]

        kst_timezone = timezone(timedelta(hours=9))
        sunrise = datetime.fromtimestamp(sunrise_timestamp, tz=kst_timezone).strftime(
            "%H:%M"
        )
        sunset = datetime.fromtimestamp(sunset_timestamp, tz=kst_timezone).strftime(
            "%H:%M"
        )

        weather_info = WeatherInfo(
            main=weather_data["weather"][0]["main"],
            icon=weather_data["weather"][0]["icon"],
            temp=weather_data["main"]["temp"],
            sunrise=sunrise,
            sunset=sunset,
        )

        # logger.info(f"Processed weather info: {weather_info}")
        return weather_info

    except requests.RequestException as e:
        error_msg = f"Failed to fetch weather data: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=503, detail=error_msg)

    except (KeyError, ValueError) as e:
        error_msg = f"Error processing weather data: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)

    except Exception as e:
        error_msg = f"Weather service error: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


def get_pm_info_by_city_name(lat: float, lng: float, lang: str = "kr") -> AqiInfo:
    try:
        apikey = os.getenv("OPENWEATHERMAP_API_KEY")

        if not apikey:
            raise HTTPException(
                status_code=500,
                detail="Weather API key not found in environment variables.",
            )

        # logger.info(f"Requesting weather data for lat={lat}, lng={lng}")

        # OpenWeatherMap의 미세먼지 정보 API (위도 및 경도 기준)
        api_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lng}&appid={apikey}"

        # API 요청
        result = requests.get(api_url)
        # logger.info(f"air_result: {result.text}")

        # 상태 코드 확인
        if result.status_code != 200:
            raise HTTPException(
                status_code=result.status_code,
                detail=f"Weather API Error: {result.text}",
            )

        # JSON 결과 출력
        aqi = result.json()["list"][0]["main"]["aqi"]

        # 공기질 설명 추가
        air_quality_descriptions = {
            1: "아주 좋음",
            2: "보통",
            3: "보통",
            4: "나쁨",
            5: "매우 나쁨",
        }

        air_quality_description = air_quality_descriptions.get(aqi, "정보 없음")

        return AqiInfo(aqi=aqi, description=air_quality_description)

    except requests.RequestException as e:
        error_msg = f"Failed to fetch weather AQI data: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=503, detail=error_msg)

    except (KeyError, ValueError) as e:
        error_msg = f"Error processing weather AQI data: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)

    except Exception as e:
        error_msg = f"Weather service AQI error: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


def get_currnet_datetime() -> str:
    try:
        timezone = pytz.timezone("Asia/Seoul")
        current_time = datetime.now(timezone)

        week_days = {
            0: "월",  # Monday
            1: "화",  # Tuesday
            2: "수",  # Wednesday
            3: "목",  # Thursday
            4: "금",  # Friday
            5: "토",  # Saturday
            6: "일",  # Sunday
        }

        day_of_week = week_days[current_time.weekday()]

        result = current_time.strftime(f"%m.%d({day_of_week}) %I:%M%p")

        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreBasicInfo Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Service LocalStoreBasicInfo Error: {str(e)}"
        )


def select_store_coordinate_by_store_business_number(
    store_business_id: str,
) -> LocalStoreCoordinate:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_store_coordinate_by_store_business_number(store_business_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreCoordinate Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Service LocalStoreCoordinate Error: {str(e)}"
        )


def get_store_local_tour_info_by_lat_lng(lat: float, lng: float):
    try:
        apikey = os.getenv("TOUR_API_SERVICE_KEY")
        if not apikey:
            raise HTTPException(
                status_code=500,
                detail="TOUR API key not found in environment variables.",
            )

        session = requests.Session()
        session.mount("https://", TLSAdapter())

        api_url = "https://apis.data.go.kr/B551011/KorService1/locationBasedList1"

        # logger.info(f"lat: {lat}, lng: {lng}")

        params = {
            "numOfRows": 10,
            "pageNo": 1,
            "MobileOS": "ETC",
            "MobileApp": "AppTest",
            "_type": "json",
            "listYN": "Y",
            "arrange": "A",
            "mapX": lng,
            "mapY": lat,
            "radius": 1500,
            "serviceKey": apikey,
        }

        tour_response = session.get(api_url, params=params, timeout=10)

        # logger.info(f"응답 상태 코드: {tour_response.status_code}")
        # logger.info(f"요청 URL: {tour_response.url}")

        tour_response.raise_for_status()

        tour_data = tour_response.json()
        # logger.info(f"Tour 데이터 응답: {tour_data}")

        return tour_data

    except requests.exceptions.SSLError as ssl_err:
        logger.error(f"SSL 인증 오류: {ssl_err}")
        raise HTTPException(status_code=503, detail=f"SSL 인증 오류: {ssl_err}")

    except requests.exceptions.RequestException as e:
        logger.error(f"tour 데이터 요청 실패: {e}")
        raise HTTPException(status_code=503, detail=f"tour 데이터 요청 실패: {e}")

    except Exception as e:
        logger.error(f"tour 서비스 오류: {e}")
        raise HTTPException(status_code=500, detail=f"tour 서비스 오류: {e}")


def get_road_event_info_by_lat_lng(lat: float, lng: float):
    try:
        apikey = os.getenv("ROAD_API_SERVICE_KEY")
        if not apikey:
            raise HTTPException(
                status_code=500,
                detail="Road API key not found in environment variables.",
            )

        maxX = lng + 0.015  # 약 1500m
        maxY = lat + 0.015  # 약 1500m

        api_url = f"https://openapi.its.go.kr:9443/eventInfo?apiKey={apikey}&type=all&eventType=all&minX={lng}&maxX={maxX}&minY={lat}&maxY={maxY}&getType=json"

        # logger.info(f"Requesting Road data for lat={lat}, lng={lng}")
        # logger.info(f"Requesting Road data for api_url: {api_url}")
        road_event_response = requests.get(api_url)
        road_event_data = road_event_response.json()

        if road_event_response.status_code != 200:
            error_msg = f"road_event API Error: {road_event_data.get('message', 'Unknown error')}"
            logger.error(error_msg)
            raise HTTPException(
                status_code=road_event_response.status_code, detail=error_msg
            )

        # logger.info(f"road_event API response: {road_event_data}")

        # logger.info(f"Processed road_event info: {road_event_info}")
        return road_event_response.json()

    except requests.RequestException as e:
        error_msg = f"Failed to fetch road_event data: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=503, detail=error_msg)

    except (KeyError, ValueError) as e:
        error_msg = f"Error processing road_event data: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)

    except Exception as e:
        error_msg = f"road_event service error: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)