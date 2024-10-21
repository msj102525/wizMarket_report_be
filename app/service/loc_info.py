from fastapi import HTTPException
from app.crud.loc_info import *

from app.crud.loc_store import (
    select_local_store_sub_distirct_id_by_store_business_number as crud_select_local_store_sub_distirct_id_by_store_business_number,
)
from app.crud.statistics import (
    select_nationwide_jscore_by_stat_item_id_and_sub_district_id as crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id,
    select_state_item_id as crud_select_state_item_id,
)
from app.schemas.loc_store import LocalStoreSubdistrict
from app.schemas.statistics import (
    DataRefDateSubDistrictName,
    LocInfoStatisticsDataRefOutput,
    LocInfoStatisticsOutput,
)


def select_report_loc_info_by_store_business_number(
    store_business_id: str,
) -> LocInfoStatisticsDataRefOutput:

    try:
        local_store_sub_district_data: LocalStoreSubdistrict = (
            crud_select_local_store_sub_distirct_id_by_store_business_number(
                store_business_id
            )
        )

        print(local_store_sub_district_data)

        sub_district_id = local_store_sub_district_data.get("SUB_DISTRICT_ID")
        sub_district_name = local_store_sub_district_data.get("SUB_DISTRICT_NAME")

        # sub_district_id가 None일 경우 오류 처리
        if sub_district_id is None:
            raise HTTPException(status_code=500, detail="Sub-district ID not found.")

        # 각 통계 항목 ID 조회 및 출력
        mz_pupulation_stat_item_id: int = crud_select_state_item_id(
            "population", "mz_population"
        )
        # print(f"mz_pupulation_stat_item_id: {mz_pupulation_stat_item_id}")

        resident_stat_item_id: int = crud_select_state_item_id("loc_info", "resident")
        # print(f"resident_stat_item_id: {resident_stat_item_id}")

        move_pop_stat_item_id: int = crud_select_state_item_id("loc_info", "move_pop")
        # print(f"move_pop_stat_item_id: {move_pop_stat_item_id}")

        house_stat_item_id: int = crud_select_state_item_id("loc_info", "house")
        # print(f"house_stat_item_id: {house_stat_item_id}")

        shop_stat_item_id: int = crud_select_state_item_id("loc_info", "shop")
        # print(f"shop_stat_item_id: {shop_stat_item_id}")

        income_stat_item_id: int = crud_select_state_item_id("loc_info", "income")
        # print(f"income_stat_item_id: {income_stat_item_id}")

        spend_stat_item_id: int = crud_select_state_item_id("loc_info", "spend")
        # print(f"spend_stat_item_id: {spend_stat_item_id}")

        sales_stat_item_id: int = crud_select_state_item_id("loc_info", "sales")
        # print(f"sales_stat_item_id: {sales_stat_item_id}")

        # print(f"loc_info: {store_business_id}")
        # print(f"loc_info: {sub_district_id}")

        # 각 통계 데이터 조회 및 처리
        mz_population_jscore: float = round(
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                mz_pupulation_stat_item_id, sub_district_id
            ).get("J_SCORE"),
            1,
        )
        shop_jscore: float = round(
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                shop_stat_item_id, sub_district_id
            ).get("J_SCORE"),
            1,
        )
        move_pop_jscore: float = round(
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                move_pop_stat_item_id, sub_district_id
            ).get("J_SCORE"),
            1,
        )
        resident_jscore: float = round(
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                resident_stat_item_id, sub_district_id
            ).get("J_SCORE"),
            1,
        )
        house_jscore: float = round(
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                house_stat_item_id, sub_district_id
            ).get("J_SCORE"),
            1,
        )
        income_jscore: float = round(
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                income_stat_item_id, sub_district_id
            ).get("J_SCORE"),
            1,
        )
        spend_jscore: float = round(
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                spend_stat_item_id, sub_district_id
            ).get("J_SCORE"),
            1,
        )
        sales_jscore: float = round(
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                sales_stat_item_id, sub_district_id
            ).get("J_SCORE"),
            1,
        )
        data_ref_date: date = (
            crud_select_nationwide_jscore_by_stat_item_id_and_sub_district_id(
                mz_pupulation_stat_item_id, sub_district_id
            ).get("REF_DATE")
        )

        data_ref = DataRefDateSubDistrictName(
            sub_district_name=sub_district_name, reference_date=data_ref_date
        )

        # print(data_ref)

        # 각 stat_item_id와 jscore 출력
        # print(f"mz_population_jscore: {mz_population_jscore}")
        # print(f"shop_jscore: {shop_jscore}")
        # print(f"move_pop_jscore: {move_pop_jscore}")
        # print(f"resident_jscore: {resident_jscore}")
        # print(f"house_jscore: {house_jscore}")
        # print(f"income_jscore: {income_jscore}")
        # print(f"spend_jscore: {spend_jscore}")
        # print(f"sales_jscore: {sales_jscore}")

        loc_info_report_data = LocInfoStatisticsOutput(
            mz_population_jscore=mz_population_jscore,
            shop_jscore=shop_jscore,
            move_pop_jscore=move_pop_jscore,
            resident_jscore=resident_jscore,
            house_jscore=house_jscore,
            income_jscore=income_jscore,
            spend_jscore=spend_jscore,
            sales_jscore=sales_jscore,
        )

        loc_info_report_output = LocInfoStatisticsDataRefOutput(
            loc_info=loc_info_report_data, data_ref=data_ref
        )

        return loc_info_report_output

    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
