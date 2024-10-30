import logging
from dotenv import load_dotenv
from fastapi import HTTPException


from app.crud.rising_business import (
    select_rising_business_by_store_business_id as crud_select_rising_business_by_store_business_id,
)
from app.schemas.report import (
    LocalStoreRisingBusinessNTop5SDTop3,
)

logger = logging.getLogger(__name__)


def select_rising_business_by_store_business_id(
    store_business_id: str,
) -> LocalStoreRisingBusinessNTop5SDTop3:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_rising_business_by_store_business_id(store_business_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreRisingBusinessNTop5SDTop3 Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreRisingBusinessNTop5SDTop3 Error: {str(e)}",
        )
