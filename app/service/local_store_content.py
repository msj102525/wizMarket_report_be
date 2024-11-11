import logging
from typing import List
from fastapi import HTTPException

from app.crud.local_store_content import (
    select_local_store_content_by_store_business_number as crud_select_local_store_content_by_store_business_number,
    select_biz_detail_category_id_list_by_store_business_number as crud_select_biz_detail_category_id_list_by_store_business_number,
    select_detail_category_content_by_biz_detail_category_id_list as crud_select_detail_category_content_by_biz_detail_category_id_list,
)
from app.schemas.report import BizDetailCategoryContent, LocalStoreContent


logger = logging.getLogger(__name__)


def select_local_store_content_by_store_business_number(
    store_business_id: str,
) -> List[LocalStoreContent]:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        return crud_select_local_store_content_by_store_business_number(
            store_business_id
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreContent Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service LocalStoreContent Error: {str(e)}",
        )


def select_detail_category_content_by_store_business_number(
    store_business_id: str,
) -> List[BizDetailCategoryContent]:
    # logger.info(f"Fetching store info for business ID: {store_business_id}")

    try:
        detail_category_id_list = (
            crud_select_biz_detail_category_id_list_by_store_business_number(
                store_business_id
            )
        )
        # logger.info(f"detail_category_id_list: {detail_category_id_list}")

        return crud_select_detail_category_content_by_biz_detail_category_id_list(
            detail_category_id_list
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service BizDetailCategoryContent Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service BizDetailCategoryContent Error: {str(e)}",
        )
