import logging
from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.responses import PlainTextResponse

from app.schemas.common_information import CommonInformationOutput
from app.schemas.report import (
    AqiInfo,
    BizDetailCategoryContent,
    LocalStoreCDCommercialDistrict,
    LocalStoreCDDistrictAverageSalesTop5,
    LocalStoreCDJSWeightedAverage,
    LocalStoreCDTiemAverageSalesPercent,
    LocalStoreCDWeekdayAverageSalesPercent,
    LocalStoreCommercialDistrictJscoreAverage,
    LocalStoreContent,
    LocalStoreCoordinate,
    LocalStoreInfoWeaterInfoOutput,
    LocalStoreLIJSWeightedAverage,
    LocalStoreLocInfoJscoreData,
    LocalStoreLocInfoJscoreDataOutput,
    LocalStoreMainCategoryCount,
    LocalStoreMovePopData,
    LocalStorePopulationDataOutPut,
    LocalStoreRedux,
    LocalStoreResidentWorkPopData,
    LocalStoreRisingBusinessNTop5SDTop3Output,
    LocalStoreTop5Menu,
    LocalStoreTop5MenuAdviceOutput,
    WeatherInfo,
    GPTAnswer,
)
from app.service.local_store_basic_info import (
    get_road_event_info_by_lat_lng,
    get_store_local_tour_info_by_lat_lng,
    select_local_store_info_redux_by_store_business_number as service_select_local_store_info_redux_by_store_business_number,
    get_weather_info_by_lat_lng as service_get_weather_info_by_lat_lng,
    get_pm_info_by_city_name as service_get_pm_info_by_city_name,
    get_currnet_datetime as service_get_currnet_datetime,
    select_store_coordinate_by_store_business_number as service_select_store_coordinate_by_store_business_number,
)
from app.service.local_store_basic_info import (
    select_local_store_info_by_store_business_number as service_select_local_store_info_by_store_business_number,
)
from app.service.common_information import (
    get_all_report_common_information as service_get_all_report_common_information,
)
from app.service.population import (
    select_population_by_store_business_number as service_select_population_by_store_business_number,
)
from app.service.loc_info import (
    select_loc_info_j_score_average_by_store_business_number as select_select_loc_info_j_score_average_by_store_business_number,
    select_loc_info_j_score_by_store_business_number as service_select_loc_info_j_score_by_store_business_number,
    select_loc_info_resident_work_compare_by_store_business_number as service_select_loc_info_resident_work_compare_by_store_business_number,
    select_loc_info_move_pop_by_store_business_number as service_select_loc_info_move_pop_by_store_business_number,
)
from app.service.commercial_district import (
    select_rising_menu_top5_by_store_business_number as service_select_rising_menu_top5_by_store_business_number,
    select_c_d_j_score_average_by_store_business_number as service_select_c_d_j_score_average_by_store_business_number,
    select_commercial_district_j_score_by_store_business_number as service_select_commercial_district_j_score_by_store_business_number,
    select_commercial_district_weekday_average_sales_by_store_business_number as service_select_commercial_district_weekday_average_sales_by_store_business_number,
    select_commercial_district_time_average_sales_by_store_business_number as service_select_commercial_district_time_average_sales_by_store_business_number,
    select_commercial_district_rising_sales_by_store_business_number as service_select_commercial_district_rising_sales_by_store_business_number,
    select_commercial_district_commercial_district_by_store_business_number as service_select_commercial_district_commercial_district_by_store_business_number,
)
from app.service.commercial_district import (
    select_c_d_main_category_count_by_store_business_number as service_select_c_d_main_category_count_by_store_business_number,
)
from app.service.rising_business import (
    select_rising_business_by_store_business_id as service_select_rising_business_by_store_business_id,
)
from app.service.local_store_content import (
    select_local_store_content_by_store_business_number as service_select_local_store_content_by_store_business_number,
    select_detail_category_content_by_store_business_number as service_select_detail_category_content_by_store_business_number,
)


from app.service.gpt_answer import (
    get_rising_business_gpt_answer_by_local_store_top5_menu as service_get_rising_business_gpt_answer_by_local_store_top5_menu,
    get_loc_info_gpt_answer_by_local_store_loc_info as service_get_loc_info_gpt_answer_by_local_store_loc_info,
    get_rising_business_gpt_answer_by_rising_business as service_get_rising_business_gpt_answer_by_rising_business,
    get_commercial_district_gpt_answer_by_cd_j_score_average as service_get_commercial_district_gpt_answer_by_cd_j_score_average,
    get_store_info_gpt_answer_by_store_info as service_get_store_info_gpt_answer_by_store_info,
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/store/info/redux", response_model=LocalStoreRedux)
def select_report_store_info_redux(store_business_id: str):

    # logger.info(
    #     f"Received request for store info with business ID: {store_business_id}"
    # )

    try:
        # logger.info(
        #     f"Successfully retrieved store info for business ID: {store_business_id}"
        # )

        return service_select_local_store_info_redux_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        # service 계층에서 발생한 HTTP 예외는 그대로 전달
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    # except ValueError as ve:
    #     # 입력값 검증 실패 등의 에러
    #     error_msg = f"Invalid input: {str(ve)}"
    #     logger.error(error_msg)
    #     raise HTTPException(status_code=422, detail=error_msg)

    except Exception as e:
        # 예상치 못한 에러
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/store/info", response_model=LocalStoreInfoWeaterInfoOutput)
def select_report_store_info(store_business_id: str):
    # logger.info(
    #     f"Received request for store info with business ID: {store_business_id}"
    # )

    try:
        # logger.info(
        #     f"Successfully retrieved store info for business ID: {store_business_id}"
        # )

        local_store_info = service_select_local_store_info_by_store_business_number(
            store_business_id
        )

        # logger.info(f"local_store_info{local_store_info}")
        # logger.info(f"local_store_info.latitude{local_store_info.latitude}")
        # logger.info(f"local_store_info.longitude{local_store_info.longitude}")

        weather_data: WeatherInfo = service_get_weather_info_by_lat_lng(
            local_store_info.latitude, local_store_info.longitude
        )

        # logger.info(f"weather_data: {weather_data}")

        pm_data: AqiInfo = service_get_pm_info_by_city_name(
            local_store_info.latitude, local_store_info.longitude
        )
        # logger.info(f"pm_data: {pm_data}")

        format_current_datetime: str = service_get_currnet_datetime()

        store_all_data = LocalStoreInfoWeaterInfoOutput(
            localStoreInfo=local_store_info,
            weatherInfo=weather_data,
            aqi_info=pm_data,
            format_current_datetime=format_current_datetime,
        )

        # GPT ###########################################################################
        # store_advice: GPTAnswer = service_get_store_info_gpt_answer_by_store_info(store_all_data)
        # GPT ###########################################################################

        # store_advice_dummy = """Dummy
        #                         1.점심 시간대 집중 전략
        #                         분평동에서 가장 매출이 높은 시간대는 12시부터 15시 사이입니다. 이 시간에 특별 메뉴나 할인 이벤트로 고객을 유치해보세요.
        #                             2.	주말 프로모션 강화
        #                         토요일에 매출이 가장 높으니, 주말에 가족 단위 고객을 대상으로 하는 패키지 프로모션을 고려하세요.
        #                             3.	IT 기술 활용한 예약 시스템 최적화
        #                         IT에 익숙하시면, 예약 시스템을 강화해 고객 대기 시간을 줄이고, 방문 경험을 더욱 편리하게 만드세요.
        #                             4.	50대 여성 고객 맞춤 서비스 제공
        #                         가장 큰 고객층인 50대 여성을 위한 특별한 메뉴나 세트 구성, VIP 프로그램 등을 도입하여 고객 충성도를 높이세요.
        #                             5.	날씨에 맞춘 테라스 좌석 활용
        #                         오늘처럼 맑은 날씨에는 테라스나 창가 자리를 강조해 고객에게 특별한 분위기를 제공하세요.
        #                         """
        store_advice_dummy = """Dummy 
                                오늘의 장사지수:41%

                                오늘은 추운 날씨와 월요일로 인해 30-40대 남성고객 유동인구수가 적어 유입이 많지 않을 것으로 보입니다.
                                """

        result = LocalStoreInfoWeaterInfoOutput(
            localStoreInfo=local_store_info,
            weatherInfo=weather_data,
            aqi_info=pm_data,
            format_current_datetime=format_current_datetime,
            # store_info_advice=store_advice.gpt_answer, #GPT
            store_info_advice=store_advice_dummy,  # Dummy
        )
        return result

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


# RisingMenu
@router.get("/rising/menu/advice", response_model=LocalStoreTop5MenuAdviceOutput)
def get_report_rising_menu_gpt(
    store_business_id: str,
):
    # logger.info(
    #     f"Received request for store info with business ID: {store_business_id}"
    # )

    try:
        # logger.info(
        #     f"Successfully retrieved store info for business ID: {store_business_id}"
        # )

        rising_menu_top5: LocalStoreTop5Menu = (
            service_select_rising_menu_top5_by_store_business_number(store_business_id)
        )
        # logger.info(f"rising_menu_top5: {rising_menu_top5}")

        # GPT ###########################################################################
        # report_advice = service_get_rising_business_gpt_answer_by_local_store_top5_menu(rising_menu_top5) # GPT API
        # logger.info(f"report_advice: {report_advice}")
        # GPT ###########################################################################

        report_dummy = """
                        Dummy Data
                        삼겹살이랑 돼지갈비가 인기가 많으니까,
                        그 두 가지를 묶어서 세트 메뉴로 한번 내봐유.
                        금요일엔 사람들이 술도 많이 먹으니까 병맥주나
                        소주 할인 이벤트 하나 해주면 딱 좋을 거여.
                        된장찌개는 그냥 기본으로 맛있게 준비해주면 손님들 만족도가 더 높아질 거유!
                        """

        result = LocalStoreTop5MenuAdviceOutput(
            local_store_top5_orderd_menu=rising_menu_top5,
            # rising_menu_advice=report_advice.gpt_answer, # GPT API
            rising_menu_advice=report_dummy,  # Dummy
        )

        return result

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/common/info", response_model=List[CommonInformationOutput])
def select_all_report_common_information():
    try:
        return service_get_all_report_common_information()
    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/population", response_model=LocalStorePopulationDataOutPut)
def select_population_data(store_business_id: str):
    try:

        return service_select_population_by_store_business_number(store_business_id)

        # GPT ###########################################################################
        # report_advice = service_get_rising_business_gpt_answer_by_local_store_top5_menu(rising_menu_top5) # GPT API
        # logger.info(f"report_advice: {report_advice}")
        # GPT ###########################################################################

        report_dummy = """
                        Dummy Data
                        삼겹살이랑 돼지갈비가 인기가 많으니까,
                        그 두 가지를 묶어서 세트 메뉴로 한번 내봐유.
                        금요일엔 사람들이 술도 많이 먹으니까 병맥주나
                        소주 할인 이벤트 하나 해주면 딱 좋을 거여.
                        된장찌개는 그냥 기본으로 맛있게 준비해주면 손님들 만족도가 더 높아질 거유!
                        """

        result = LocalStoreTop5MenuAdviceOutput(
            local_store_top5_orderd_menu=rising_menu_top5,
            # rising_menu_advice=report_advice.gpt_answer, # GPT API
            rising_menu_advice=report_dummy,  # Dummy
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/location/jscore/average", response_model=LocalStoreLIJSWeightedAverage)
def select_loc_info_j_score_average_by_store_business_number(store_business_id: str):
    try:
        return select_select_loc_info_j_score_average_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/location/jscore", response_model=LocalStoreLocInfoJscoreDataOutput)
def select_loc_info_j_scorereport_data(store_business_id: str):
    try:

        local_store_loc_info_data: LocalStoreLocInfoJscoreData = (
            service_select_loc_info_j_score_by_store_business_number(store_business_id)
        )

        # logger.info(f"local_store_loc_info_data: {local_store_loc_info_data}")

        # GPT ###########################################################################
        # report_advice: GPTAnswer = (
        #     service_get_loc_info_gpt_answer_by_local_store_loc_info(
        #         local_store_loc_info_data
        #     )
        # )
        # GPT ###########################################################################
        report_dummy = """Dummy Data
                                결론
                                전국적 트렌드와 지역 매출 증가업종 데이터를 바탕으로, **이자카야의 인기를 반영한 프리미엄 주류와 삼겹살의 결합** 및 **젊은층을 겨냥한 효율적인 메뉴 제공**이 당산2동에서 성공적인 전략이 될 수 있습니다.
                                또한 **배달 및 테이크아웃 강화**는 실용적인 소비 경향을 반영한 중요한 요소가 될 것입니다.
                        """

        result = LocalStoreLocInfoJscoreDataOutput(
            local_store_loc_info_j_score_data=local_store_loc_info_data,
            # loc_info_advice=report_advice.gpt_answer,
            loc_info_advice=report_dummy,
        )

        return result

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/location/resident/work/compare", response_model=LocalStoreResidentWorkPopData
)
def select_loc_info_resident_work_compare_by_store_business_number(
    store_business_id: str,
):
    # print(store_business_id)
    try:
        return service_select_loc_info_resident_work_compare_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/commercialDistrict/jscore/average", response_model=LocalStoreCDJSWeightedAverage
)
def select_c_d_j_score_average_by_store_business_number(store_business_id: str):
    # print(store_business_id)
    try:
        return service_select_c_d_j_score_average_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/location/move/population", response_model=LocalStoreMovePopData)
def select_loc_info_move_pop_by_store_business_number(store_business_id: str):
    # print(store_business_id)
    try:
        return service_select_loc_info_move_pop_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/commercialDistrict/mainCategory/count", response_model=LocalStoreMainCategoryCount
)
def select_c_d_main_category_count_by_store_business_number(store_business_id: str):
    # print(store_business_id)
    try:
        return service_select_c_d_main_category_count_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/commercialDistrict/jscore",
    response_model=LocalStoreCommercialDistrictJscoreAverage,
)
def select_commercial_district_j_score_by_store_business_number(store_business_id: str):
    # print(store_business_id)
    try:

        cd_j_score_data = (
            service_select_commercial_district_j_score_by_store_business_number(
                store_business_id
            )
        )

        return cd_j_score_data

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/commercialDistrict/weekday/sales",
    response_model=LocalStoreCDWeekdayAverageSalesPercent,
)
def select_commercial_district_weekday_average_sales_by_store_business_number(
    store_business_id: str,
):
    # print(store_business_id)
    try:

        return service_select_commercial_district_weekday_average_sales_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/commercialDistrict/time/sales",
    response_model=LocalStoreCDTiemAverageSalesPercent,
)
def select_commercial_district_time_average_sales_by_store_business_number(
    store_business_id: str,
):
    # print(store_business_id)
    try:

        return service_select_commercial_district_time_average_sales_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/commercialDistrict/rising/sales",
    response_model=LocalStoreCDDistrictAverageSalesTop5,
)
def select_commercial_district_rising_sales_by_store_business_number(
    store_business_id: str,
):
    # print(store_business_id)
    try:

        return service_select_commercial_district_rising_sales_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/rising/business",
    response_model=LocalStoreRisingBusinessNTop5SDTop3Output,
)
def select_rising_business_by_store_business_id(store_business_id: str):
    # print(store_business_id)
    try:

        rising_business_data = service_select_rising_business_by_store_business_id(
            store_business_id
        )

        # logger.info(f"rising_business_data: {rising_business_data}")

        # GPT ###########################################################################
        # report_advice: GPTAnswer = (
        #     service_get_rising_business_gpt_answer_by_rising_business(
        #         rising_business_data
        #     )
        # )
        # GPT ###########################################################################

        report_advice_dummy = """Dummy 
                                (1) 고급화된 메뉴 개발
                                •	초밥 전문점 트렌드에 대응:
                                •	돼지고기를 활용한 프리미엄 메뉴 개발(예: 트러플 소스를 곁들인 돼지고기 찜).
                                •	숙성 과정을 강조하여 고급 이미지를 부각.

                            (2) 국물 메뉴 추가
                                •	해장국/감자탕 트렌드에 대응:
                                •	돼지고기를 활용한 국물 메뉴(예: 돼지 등뼈찜탕, 김치찜)를 추가하여 소비자 선택의 폭을 넓힘.
                                •	술자리 후 해장용 메뉴로 활용 가능.

                            (3) 건강식 컨셉 도입
                                •	헬스클럽 트렌드에 대응:
                                •	저염식, 고단백 메뉴를 개발해 운동 후 식사로 적합한 옵션 제공.
                                •	“운동 후에도 즐길 수 있는 건강한 돼지고기 요리”를 슬로건으로 홍보.

                            (4) 직장인 공략
                                •	사무용품 트렌드와 연관된 직장인 타겟:
                                •	점심 세트 메뉴(가성비 좋은 구성)와 퇴근 후 회식 패키지를 강화.
                                •	SNS나 지역 커뮤니티를 통해 “동료와 함께하는 저녁 할인 이벤트”를 홍보.

                            (5) 지역 축산물 협력
                                •	축산물 소매 트렌드에 대응:
                                •	지역 축산물 판매점과 협업하여 ‘신선한 지역산 돼지고기’를 메뉴에 사용함을 알림.
                                •	소비자에게 신뢰를 주며 차별화된 이미지를 제공.

                            마케팅 및 프로모션 전략

                            (1) 메뉴 차별화 홍보
                                •	숙성 고기의 특장점 강조:
                                •	“정성으로 숙성한 고기로 최고의 맛을 경험하세요.”
                                •	숙성 과정 및 신선도를 시각화한 콘텐츠 제작(SNS, 홈페이지 활용).

                            (2) 고객 참여 이벤트
                                •	“프리미엄 돼지고기 체험 이벤트”를 통해 방문 고객에게 특별 메뉴 제공.
                                •	이벤트 참여 후 SNS에 리뷰를 작성한 고객에게 할인 쿠폰 증정.

                            (3) 배달 서비스 강화
                                •	국물 요리 및 돼지고기 찜과 같은 인기 메뉴를 중심으로 배달 전용 세트 메뉴 출시.
                                •	고객 리뷰 프로모션(리뷰 작성 시 할인 쿠폰 증정)으로 배달 고객 유치.

                            (4) 운동 고객 타겟
                                •	헬스클럽 주변에 운동 후 할인 쿠폰을 배포하거나 고단백 식사 추천 이벤트 진행.
                                •	건강식에 관심 있는 고객을 위한 “운동 후 한 끼” 홍보.
                            """

        result = LocalStoreRisingBusinessNTop5SDTop3Output(
            rising_business_data=rising_business_data,
            # rising_business_advice = report_advice.gpt_answer,
            rising_business_advice=report_advice_dummy,
        )

        return result

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/commercialDistrict",
    response_model=LocalStoreCDCommercialDistrict,
)
def select_commercial_district_commercial_district_by_store_business_number(
    store_business_id: str,
):
    # print(store_business_id)
    try:

        return service_select_commercial_district_commercial_district_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/local/store/content",
    response_model=List[LocalStoreContent],
)
def select_local_store_content_by_store_business_number(
    store_business_id: str,
):
    # print(store_business_id)
    try:

        return service_select_local_store_content_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get(
    "/detail/category/content",
    response_model=List[BizDetailCategoryContent],
)
def select_detail_category_content_by_store_business_number(
    store_business_id: str,
):
    # print(store_business_id)
    try:
        return service_select_detail_category_content_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/local/tour/info")
def select_store_local_tour_info(store_business_id: str):
    # logger.info(
    #     f"Received request for store info with business ID: {store_business_id}"
    # )

    try:
        # logger.info(
        #     f"Successfully retrieved store info for business ID: {store_business_id}"
        # )

        local_store_coordinate: LocalStoreCoordinate = (
            service_select_store_coordinate_by_store_business_number(store_business_id)
        )

        # logger.info(
        #     f"local_store_coordinate: {local_store_coordinate}"
        # )

        tour_info = get_store_local_tour_info_by_lat_lng(
            local_store_coordinate.latitude, local_store_coordinate.longitude
        )

        return tour_info

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get("/local/road/info")
def select_store_road_tour_info(store_business_id: str):
    # logger.info(
    #     f"Received request for store info with business ID: {store_business_id}"
    # )

    try:
        # logger.info(
        #     f"Successfully retrieved store info for business ID: {store_business_id}"
        # )

        local_store_coordinate: LocalStoreCoordinate = (
            service_select_store_coordinate_by_store_business_number(store_business_id)
        )

        # logger.info(
        #     f"local_store_coordinate: {local_store_coordinate}"
        # )

        road_info = get_road_event_info_by_lat_lng(
            local_store_coordinate.latitude, local_store_coordinate.longitude
        )

        return road_info

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)
