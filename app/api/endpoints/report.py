import logging
from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.responses import PlainTextResponse

from app.schemas.common_information import CommonInformationOutput
from app.schemas.report import (
    AqiInfo,
    LocalStoreCDCommercialDistrict,
    LocalStoreCDDistrictAverageSalesTop5,
    LocalStoreCDJSWeightedAverage,
    LocalStoreCDTiemAverageSalesPercent,
    LocalStoreCDWeekdayAverageSalesPercent,
    LocalStoreCommercialDistrictJscoreAverage,
    LocalStoreInfoWeaterInfoOutput,
    LocalStoreLIJSWeightedAverage,
    LocalStoreLocInfoJscoreData,
    LocalStoreMainCategoryCount,
    LocalStoreMovePopData,
    LocalStorePopulationDataOutPut,
    LocalStoreRedux,
    LocalStoreResidentWorkPopData,
    LocalStoreRisingBusinessNTop5SDTop3,
    LocalStoreTop5Menu,
    LocalStoreTop5MenuAdviceOutput,
    WeatherInfo,
    GPTAnswer,
)
from app.service.local_store_basic_info import (
    select_local_store_info_redux_by_store_business_number as service_select_local_store_info_redux_by_store_business_number,
    get_weather_info_by_lat_lng as service_get_weather_info_by_lat_lng,
    get_pm_info_by_city_name as service_get_pm_info_by_city_name,
    get_currnet_datetime as service_get_currnet_datetime,
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
    select_commercial_district_commercial_district_by_store_business_number as crud_select_commercial_district_commercial_district_by_store_business_number,
)
from app.service.commercial_district import (
    select_c_d_main_category_count_by_store_business_number as service_select_c_d_main_category_count_by_store_business_number,
)
from app.service.rising_business import (
    select_rising_business_by_store_business_id as service_select_rising_business_by_store_business_id,
)

from app.service.gpt_answer import (
    get_rising_business_gpt_answer_by_local_store_top5_menu as service_get_rising_business_gpt_answer_by_local_store_top5_menu,
    get_loc_info_gpt_answer_by_local_store_loc_info as service_get_loc_info_gpt_answer_by_local_store_loc_info,
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

        response_data = LocalStoreInfoWeaterInfoOutput(
            localStoreInfo=local_store_info,
            weatherInfo=weather_data,
            aqi_info=pm_data,
            format_current_datetime=format_current_datetime,
        )
        return response_data

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

        # report_advice = service_get_rising_business_gpt_answer_by_local_store_top5_menu(rising_menu_top5) # GPT API
        # logger.info(f"report_advice: {report_advice}")

        report_dummy = """Dummy Data<br/> 삼겹살이랑 돼지갈비가 인기가 많으니까,<br/> 그 두 가지를 묶어서 세트 메뉴로 한번 내봐유.<br/>금요일엔 사람들이 술도 많이 먹으니까 병맥주나<br/>소주 할인 이벤트 하나 해주면 딱 좋을 거여.<br/>된장찌개는 그냥 기본으로 맛있게 준비해주면 손님들 만족도가 더 높아질 거유!"""

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


@router.get("/location/jscore", response_model=LocalStoreLocInfoJscoreData)
def select_loc_info_j_scorereport_data(store_business_id: str):
    try:

        local_store_loc_info_data = (
            service_select_loc_info_j_score_by_store_business_number(store_business_id)
        )

        # logger.info(f"local_store_loc_info_data: {local_store_loc_info_data}")

        # report_advice = service_get_loc_info_gpt_answer_by_local_store_loc_info(local_store_loc_info_data)

        return local_store_loc_info_data

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

        return service_select_commercial_district_j_score_by_store_business_number(
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
    response_model=LocalStoreRisingBusinessNTop5SDTop3,
)
def select_rising_business_by_store_business_id(store_business_id: str):
    # print(store_business_id)
    try:

        return service_select_rising_business_by_store_business_id(store_business_id)

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

        return crud_select_commercial_district_commercial_district_by_store_business_number(
            store_business_id
        )

    except HTTPException as http_ex:
        logger.error(f"HTTP error occurred: {http_ex.detail}")
        raise http_ex

    except Exception as e:
        error_msg = f"Unexpected error while processing request: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)
