import logging
from dotenv import load_dotenv
from fastapi import HTTPException


from app.schemas.report import (
    LocalStoreLIJSWeightedAverage,
    LocalStoreLocInfoDistrictHotPlaceTop5,
    LocalStoreLocInfoJscoreData,
    LocalStoreMovePopData,
    LocalStoreResidentWorkPopData,
)
from app.crud.loc_info import (
    select_loc_info_j_score_average_by_store_business_number as crud_select_loc_info_j_score_average_by_store_business_number,
    select_loc_info_j_score_by_store_business_number as crud_select_loc_info_j_score_by_store_business_number,
    select_loc_info_resident_work_compare_by_store_business_number as crud_select_loc_info_resident_work_compare_by_store_business_number,
    select_loc_info_move_pop_by_store_business_number as crud_select_loc_info_move_pop_by_store_business_number,
    select_loc_info_hot_place_top5_by_store_business_number as crud_select_loc_info_hot_place_top5_by_store_business_number,
)


logger = logging.getLogger(__name__)


def select_loc_info_j_score_average_by_store_business_number(
    store_business_id: str,
) -> LocalStoreLIJSWeightedAverage:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_loc_info_j_score_average_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreLIJSWeightedAverage Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreLIJSWeightedAverage Error: {str(e)}",
        )


def select_loc_info_j_score_by_store_business_number(
    store_business_id: str,
) -> LocalStoreLocInfoJscoreData:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_loc_info_j_score_by_store_business_number(store_business_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreLocInfoJscoreData Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreLocInfoJscoreData Error: {str(e)}",
        )


def select_loc_info_resident_work_compare_by_store_business_number(
    store_business_id: str,
) -> LocalStoreResidentWorkPopData:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_loc_info_resident_work_compare_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreResidentWorkPopData Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreResidentWorkPopData Error: {str(e)}",
        )


def select_loc_info_resident_work_compare_by_store_business_number(
    store_business_id: str,
) -> LocalStoreResidentWorkPopData:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_loc_info_resident_work_compare_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreResidentWorkPopData Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreResidentWorkPopData Error: {str(e)}",
        )


def select_loc_info_move_pop_by_store_business_number(
    store_business_id: str,
) -> LocalStoreMovePopData:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_loc_info_move_pop_by_store_business_number(store_business_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreMovePopData Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreMovePopData Error: {str(e)}",
        )


def select_loc_info_hot_place_top5_by_store_business_number(
    store_business_id: str,
) -> LocalStoreLocInfoDistrictHotPlaceTop5:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_loc_info_hot_place_top5_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreLocInfoDistrictHotPlaceTop5 Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreLocInfoDistrictHotPlaceTop5 Error: {str(e)}",
        )
