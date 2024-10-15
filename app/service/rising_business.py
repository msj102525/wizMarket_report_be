from typing import List
from fastapi import HTTPException

from app.crud.loc_store import (
    select_local_store_sub_distirct_id_by_store_business_number as crud_select_local_store_sub_distirct_id_by_store_business_number,
)
from app.crud.rising_business import (
    select_top5_rising_business as crud_select_top5_rising_business,
    select_top3_rising_business_by_store_business_number as crud_select_top3_rising_business_by_store_business_number,
)
from app.schemas.loc_store import LocalStoreSubdistrict
from app.schemas.rising_business import (
    RisingBusinessOutput,
)





def select_top5_rising_business() -> List[RisingBusinessOutput]:
    try:
        return crud_select_top5_rising_business()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


def select_top3_rising_business_by_store_business_number(
    store_business_id: str,
) -> List[RisingBusinessOutput]:
    try:
        local_store_sub_district_data: LocalStoreSubdistrict = (
            crud_select_local_store_sub_distirct_id_by_store_business_number(
                store_business_id
            )
        )

        sub_district_id = local_store_sub_district_data.get("SUB_DISTRICT_ID")

        if sub_district_id is None:
            raise HTTPException(status_code=404, detail="Sub-district ID not found.")
        return crud_select_top3_rising_business_by_store_business_number(
            sub_district_id
        )
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
