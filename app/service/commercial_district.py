import logging
from dotenv import load_dotenv
from fastapi import HTTPException


from app.crud.commercial_district import (
    select_c_d_j_score_average_by_store_business_number as crud_select_c_d_j_score_average_by_store_business_number,
    select_c_d_main_category_count_by_store_business_number as crud_select_c_d_main_category_count_by_store_business_number,
    select_commercial_district_j_score_by_store_business_number as crud_select_commercial_district_j_score_by_store_business_number,
    select_commercial_district_weekday_average_sales_by_store_business_number as crud_select_commercial_district_weekday_average_sales_by_store_business_number,
    select_commercial_district_time_average_sales_by_store_business_number as crud_select_commercial_district_time_average_sales_by_store_business_number,
)
from app.schemas.report import (
    LocalStoreCDJSWeightedAverage,
    LocalStoreCDTiemAverageSalesPercent,
    LocalStoreCDWeekdayAverageSalesPercent,
    LocalStoreCommercialDistrictJscoreAverage,
    LocalStoreMainCategoryCount,
)

logger = logging.getLogger(__name__)


def select_c_d_j_score_average_by_store_business_number(
    store_business_id: str,
) -> LocalStoreCDJSWeightedAverage:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_c_d_j_score_average_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreCDJSWeightedAverage Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreCDJSWeightedAverage Error: {str(e)}",
        )


def select_c_d_main_category_count_by_store_business_number(
    store_business_id: str,
) -> LocalStoreMainCategoryCount:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_c_d_main_category_count_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreMainCategoryCount Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreMainCategoryCount Error: {str(e)}",
        )


def select_commercial_district_j_score_by_store_business_number(
    store_business_id: str,
) -> LocalStoreCommercialDistrictJscoreAverage:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_commercial_district_j_score_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(
            f"Service LocalStoreCommercialDistrictJscoreAverage Error: {str(e)}"
        )
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreCommercialDistrictJscoreAverage Error: {str(e)}",
        )


def select_commercial_district_weekday_average_sales_by_store_business_number(
    store_business_id: str,
) -> LocalStoreCDWeekdayAverageSalesPercent:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_commercial_district_weekday_average_sales_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreCDWeekdayAverageSalesPercent Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreCDWeekdayAverageSalesPercent Error: {str(e)}",
        )


def select_commercial_district_time_average_sales_by_store_business_number(
    store_business_id: str,
) -> LocalStoreCDTiemAverageSalesPercent:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return (
            crud_select_commercial_district_time_average_sales_by_store_business_number(
                store_business_id
            )
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreCDTiemAverageSalesPercent Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreCDTiemAverageSalesPercent Error: {str(e)}",
        )
