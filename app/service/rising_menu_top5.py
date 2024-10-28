import logging
from dotenv import load_dotenv
from fastapi import HTTPException


from app.crud.rising_menu_top5 import (
    select_rising_menu_top5_by_store_business_number as crud_select_rising_menu_top5_by_store_business_number,
)
from app.schemas.report import (
    LocalStoreTop5Menu,
)

logger = logging.getLogger(__name__)


def select_rising_menu_top5_by_store_business_number(
    store_business_id: str,
) -> LocalStoreTop5Menu:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_rising_menu_top5_by_store_business_number(store_business_id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreTop5Menu Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Service LocalStoreTop5Menu Error: {str(e)}"
        )
