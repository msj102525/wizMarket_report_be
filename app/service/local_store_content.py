import logging
from typing import List
from fastapi import HTTPException

from app.crud.local_store_content import select_local_store_content_by_store_business_number as crud_select_local_store_content_by_store_business_number
from app.schemas.report import LocalStoreContent



logger = logging.getLogger(__name__)


def select_local_store_content_by_store_business_number(
    store_business_id: str,
) -> List[LocalStoreContent]:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_local_store_content_by_store_business_number(store_business_id)
        pass
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreContent Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreContent Error: {str(e)}",
        )
