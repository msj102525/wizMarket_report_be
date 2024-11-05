import logging
from typing import List
from fastapi import HTTPException

from app.schemas.common_information import CommonInformationOutput
from app.crud.common_information import (
    get_all_report_common_information as crud_get_all_report_common_information,
)

logger = logging.getLogger(__name__)


def get_all_report_common_information() -> List[CommonInformationOutput]:

    try:
        return crud_get_all_report_common_information()
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service LocalStoreTop5Menu Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Service LocalStoreTop5Menu Error: {str(e)}"
        )
