import logging
from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.responses import PlainTextResponse

from app.schemas.report import (
    AqiInfo,
    LocalStoreBasicInfo,
    LocalStoreInfoWeaterInfoOutput,
    WeatherInfo,
)
from app.service.local_store_basic_info import (
    get_pm_info_by_city_name,
    get_weather_info_by_lat_lng as service_get_weather_info_by_lat_lng,
)
from app.service.local_store_basic_info import (
    select_local_store_info_by_store_business_number as service_select_local_store_info_by_store_business_number,
)


router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/store/info", response_model=LocalStoreInfoWeaterInfoOutput)
def get_report_store_info(store_business_id: str):
    # logger.info(
    #     f"Received request for store info with business ID: {store_business_id}"
    # )

    try:
        local_store_info = service_select_local_store_info_by_store_business_number(
            store_business_id
        )
        # logger.info(
        #     f"Successfully retrieved store info for business ID: {store_business_id}"
        # )

        # logger.info(f"local_store_info{local_store_info}")
        # logger.info(f"local_store_info.latitude{local_store_info.latitude}")
        # logger.info(f"local_store_info.longitude{local_store_info.longitude}")

        weather_data: WeatherInfo = service_get_weather_info_by_lat_lng(
            local_store_info.latitude, local_store_info.longitude
        )

        # logger.info(f"weather_data: {weather_data}")

        pm_data: AqiInfo = get_pm_info_by_city_name(
            local_store_info.latitude, local_store_info.longitude
        )
        logger.info(f"pm_data: {pm_data}")

        response_data = LocalStoreInfoWeaterInfoOutput(
            localStoreInfo=local_store_info, weatherInfo=weather_data, aqi_info=pm_data
        )
        return response_data

    except HTTPException as http_ex:
        # service 계층에서 발생한 HTTP 예외는 그대로 전달
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except ValueError as ve:
        # 입력값 검증 실패 등의 에러
        error_msg = f"Invalid input: {str(ve)}"
        logger.error(error_msg)
        raise HTTPException(status_code=400, detail=error_msg)

    except Exception as e:
        # 예상치 못한 에러
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


# @router.get("/common/info", response_model=List[CommonInformationOutput])
# def get_all_report_common_information():
#     try:
#         results = service_get_all_report_common_information()
#         return results
#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal Server Error")


# @router.get("/rising", response_model=RisingBusinessNationwideTop5AndSubDistrictTop3)
# def select_rising_business_top5_top3(store_business_id: str):
#     try:
#         nationwide_top5: List[RisingBusinessOutput] = (
#             service_select_top5_rising_business()
#         )

#         sub_district_top3_data: List[RisingBusinessOutput] = (
#             service_select_top3_rising_business_by_store_business_number(
#                 store_business_id
#             )
#         )

#         result = RisingBusinessNationwideTop5AndSubDistrictTop3(
#             nationwide_top5=nationwide_top5,
#             sub_district_top3_data=sub_district_top3_data,
#         )

#         return result

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal Server Error")


# @router.get("/population", response_model=PopulationJScoreOutput)
# def select_population_report_data(store_business_id: str):
#     try:
#         sub_district_population_data = (
#             service_select_report_population_by_store_business_number(store_business_id)
#         )

#         return sub_district_population_data

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"{e}Internal Server Error")


# @router.get("/location/info", response_model=LocInfoStatisticsDataRefOutput)
# def select_loc_info_report_data(store_business_id: str):
#     # print(store_business_id)
#     try:
#         sub_district_population_data = (
#             service_select_report_loc_info_by_store_business_number(store_business_id)
#         )

#         return sub_district_population_data

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"{e}Internal Server Error")


# @router.get("/location/average/jscore", response_model=LocInfoAvgJscoreOutput)
# def select_loc_info_avg_j_score(store_business_id: str):
#     # print(store_business_id)
#     try:
#         loc_info_avg_j_score = service_select_avg_j_score(store_business_id)

#         # print(loc_info_avg_j_score)

#         return loc_info_avg_j_score

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"{e}Internal Server Error")


# @router.get("/population/compare", response_model=PopulationCompareResidentWorkPop)
# def select_population_compare_resident_work(store_business_id: str):
#     # print(store_business_id)
#     try:
#         compare_resident_work_data = service_fetch_living_env(store_business_id)

#         # print(loc_info_avg_j_score)

#         return compare_resident_work_data

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"{e}Internal Server Error")


# @router.get("/location/move_pop", response_model=LocInfoMovePop)
# def select_population_compare_resident_work(store_business_id: str):
#     # print(store_business_id)
#     try:
#         compare_resident_work_data = service_fetch_loc_info_move_pop(store_business_id)

#         # print(loc_info_avg_j_score)

#         return compare_resident_work_data

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"{e}Internal Server Error")


# # CommercialDistrictSummary
# @router.get("/gpt/report_loc_info", response_model=GPTReport)
# def generate_report_loc_info_from_gpt(store_business_id: str):
#     # print(store_business_id)
#     try:
#         # report_content = report_loc_info(store_business_id)
#         # report = PlainTextResponse(report_content)
#         report = PlainTextResponse(
#             """Dummy Daya:
#             3.5식당은 서울특별시 영등포구 신길5동에 위치한 백반/한정식 전문 음식점입니다.
#             해당 지역은 업소 수가 많지 않으며(약 3.3점), 상대적으로 높은 평균 매출(약 6.9점)과
#             중간 수준의 평균소득(약 6.2점)을 보입니다. 월 평균소비 능력과 유동인구는 평균 이하인 반면,
#             주거 인구와 세대 수는 중간 수준으로 안정적인 성향을 보입니다. 목표 고객으로는 30대에서 60대
#             이상이 주로 많은 연령대임을 고려하여 중장년층을 타깃으로 삼는 것이 유리할 것입니다.
#             운영 가이드로는 주거 인구 중심의 마케팅과 인근 거주민의 생활 패턴에 맞춘 점심 및 저녁 메뉴 특화 전략을 제안드립니다."""
#         )
#         return report

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         # 에러 로그 출력
#         print(f"Unhandled exception: {e}")
#         raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# # RisingMenu
# @router.get("/gpt/report_rising_menu", response_model=GPTReport)
# def generate_report_rising_menu_from_gpt(store_business_id: str):
#     # print(store_business_id)
#     try:
#         # report_content = report_rising_menu(store_business_id)
#         # report = PlainTextResponse(report_content)
#         report = PlainTextResponse(
#             """Dummy Data 신길5동에서 백반집 운영하신다구요?
#         좋습니다, 백반이랑 돼지고기, 소주가 뜬다니 집중할 포인트가 생겼네요!
#         첫째, '백반' 메뉴를 다양하게 준비하셔서 매일 다른 반찬으로 고객들 기대치를 높이세요.
#         둘째, 돼지고기구이랑 볶음을 잘 준비해, 식사와 술 한 잔 곁들이기 좋은 메뉴로 만드시면 손님이 자주 찾을 겁니다.
#         마지막으로는, 소고기구이는 약간의 고급 메뉴로 포지셔닝해서 가족이나 친구들끼리 모임 장소로 만들면 좋겠어요. 화이팅입니다!"""
#         )
#         return report

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"{e}Internal Server Error")


# @router.get("/gpt/report_today_tip")
# def generate_report_today_tip_from_gpt(store_business_id: str):
#     # print(store_business_id)
#     try:

#         location = service_get_lat_lng_by_store_business_id(store_business_id)
#         lat = location.latitude
#         lng = location.longitude

#         weather_data = service_get_weather_info_by_lat_lng(lat, lng)

#         weather_info = WeatherToday(
#             weather=weather_data["weather"][0]["main"],
#             temp=weather_data["main"]["temp"],
#             sunset=weather_data["sys"]["sunset"],
#         )

#         report, weather_info = report_today_tip(store_business_id, weather_info)

#         return report, weather_info

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"{e}Internal Server Error")


# # @router.get("/commercialDistrict", response_model=CommercialStatisticsData)
# @router.get("/commercialDistrict")
# def select_loc_info_report_data(store_business_id: str):
#     print(store_business_id)
#     try:
#         statistics_data = service_select_statistics_by_store_business_number(
#             store_business_id
#         )

#         return "hi"
#         return statistics_data

#     except HTTPException as http_ex:
#         raise http_ex
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"{e}Internal Server Error")
