from fastapi import HTTPException
from app.schemas.loc_store import LocalStoreInfo, LocalStoreLatLng
from app.crud.loc_store import (
    get_report_store_info_by_store_business_id as crud_get_report_store_info_by_store_business_id,
    get_lat_lng_by_store_business_id as crud_get_lat_lng_by_store_business_id,
)


def get_report_store_info_by_store_business_id(
    store_business_id: str,
) -> LocalStoreInfo:
    results = crud_get_report_store_info_by_store_business_id(store_business_id)
    if not results:
        raise HTTPException(status_code=404, detail="report loc_info not found")
    return results


def get_lat_lng_by_store_business_id(store_business_id: str) -> LocalStoreLatLng:
    results = crud_get_lat_lng_by_store_business_id(store_business_id)
    if not results:
        raise HTTPException(status_code=404, detail="report loc_info not found")
    return results
