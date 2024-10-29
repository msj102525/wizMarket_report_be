import logging
from dotenv import load_dotenv
from fastapi import HTTPException


from app.schemas.report import LocalStoreLIJSWeightedAverage
from app.crud.loc_info import (
    select_loc_info_j_score_average_by_store_business_number as crud_select_loc_info_j_score_average_by_store_business_number,
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
