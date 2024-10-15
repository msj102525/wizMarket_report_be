import requests
from fastapi import HTTPException
import os
from dotenv import load_dotenv

from app.schemas.loc_store import AqiInfo

load_dotenv()


def get_weather_info_by_lat_lng(lat: float, lng: float, lang: str = "kr") -> dict:
    try:
        apikey = os.getenv("OPENWEATHERMAP_API_KEY")

        if not apikey:
            raise HTTPException(
                status_code=500,
                detail="Weather API key not found in environment variables.",
            )

        api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={apikey}&lang={lang}&units=metric"

        result = requests.get(api_url)

        if result.status_code != 200:
            raise HTTPException(
                status_code=result.status_code,
                detail=f"Weather API Error: {result.text}",
            )

        return result.json()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Weather service error: {str(e)}")


def get_pm_info_by_city_name(lat: float, lng: float, lang: str = "kr") -> AqiInfo:
    try:
        load_dotenv()
        apikey = os.getenv("OPENWEATHERMAP_API_KEY")

        if not apikey:
            raise HTTPException(
                status_code=500,
                detail="Weather API key not found in environment variables.",
            )

        # OpenWeatherMap의 미세먼지 정보 API (위도 및 경도 기준)
        api_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lng}&appid={apikey}"

        # API 요청
        result = requests.get(api_url)

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

        air_quality_description = air_quality_descriptions.get(
            aqi, "정보 없음"
        )  # 기본값 설정

        return AqiInfo(aqi=aqi, description=air_quality_description)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Weather service error: {str(e)}")
