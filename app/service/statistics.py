import numpy as np
from tqdm import tqdm
from app.crud.biz_detail_category import (
    select_biz_detail_category_id_by_biz_detail_category_name as crud_select_biz_detail_category_id_by_biz_detail_category_name,
)
from app.crud.city import get_city_id as crud_get_city_id
from app.crud.district import get_district_id as crud_get_district_id
from app.crud.loc_store import (
    get_region_id_by_store_business_number as crud_get_region_id_by_store_business_number,
    select_local_store_sub_distirct_id_by_store_business_number as crud_select_local_store_sub_distirct_id_by_store_business_number,
)
from app.crud.stat_item import (
    select_detail_category_id_by_stat_item_id as crud_select_detail_category_id_by_stat_item_id,
    select_stat_item_info_by_stat_item_id as crud_select_stat_item_info_by_stat_item_id,
)
from app.crud.statistics import (
    select_statistics_data_by_sub_district_id_detail_category_id as crud_select_statistics_data_by_sub_district_id_detail_category_id,
)
from app.crud.statistics import *
from app.crud.sub_district import get_sub_district_id_by as crud_get_sub_district_id_by
from app.schemas.commercial_district import CommercialStatisticsData
from app.schemas.loc_store import LocalStoreSubdistrict
from app.schemas.stat_item import StatItemInfo
from app.schemas.statistics import (
    LocInfoAvgJscoreOutput,
    PopulationCompareResidentWorkPop,
)
from app.crud.stat_item import (
    select_all_stat_item_id_by_detail_category_id as crud_select_all_stat_item_id_by_detail_category_id,
)


################# 입지 정보 동 기준 가중치 평균 j_score 값 계산 ###################
# 리포트 보여주기
# div 입지분석 : x.x p
# 시/도명 시/군/구명 읍/면/동명
# '전자정부 상권정보' ref_date
def select_avg_j_score(store_business_id: str) -> LocInfoAvgJscoreOutput:

    local_store_sub_district_data: LocalStoreSubdistrict = (
        crud_select_local_store_sub_distirct_id_by_store_business_number(
            store_business_id
        )
    )

    sub_district_id = local_store_sub_district_data.get("SUB_DISTRICT_ID")

    # 1. 해당 동의 필요한 j_score 목록 가져오기
    result = get_weighted_jscore(sub_district_id)
    # result 리스트에서 J_SCORE 값만 추출
    j_scores = [item["J_SCORE"] for item in result]

    # 2. 가중치 값 적용
    shop_k = 1
    move_pop_k = 2.5
    sales_k = 1.5
    work_pop_k = 1.5
    income_k = 1.5
    spend_k = 1.5
    house_k = 1
    resident_k = 1
    mz_population_k = 1.5

    # 3. 가중치 값 적용 후 평균 계산
    weights = [
        shop_k,
        move_pop_k,
        sales_k,
        work_pop_k,
        income_k,
        spend_k,
        house_k,
        resident_k,
        mz_population_k,
    ]
    weighted_sum = sum(j_score * weight for j_score, weight in zip(j_scores, weights))
    total_weight = sum(weights)

    weighted_avg_val = weighted_sum / total_weight if total_weight != 0 else 0
    # print(weighted_avg_val)

    # 4. 이쁘게 포장
    final_item = result[0]
    del final_item["column_name"]
    del final_item["J_SCORE"]
    del final_item["table_name"]
    final_item["weighted_avg_val"] = weighted_avg_val

    # print(final_item)

    return final_item


################# 동 주거 환경 ###################
# 리포트 보여주기
# div x.x 동 주거 환경 :  ~~ % 차지
# 시/도명 시/군/구명 읍/면/동명
def fetch_living_env(store_business_id: str) -> PopulationCompareResidentWorkPop:
    local_store_sub_district_data: LocalStoreSubdistrict = (
        crud_select_local_store_sub_distirct_id_by_store_business_number(
            store_business_id
        )
    )
    sub_district_id = local_store_sub_district_data.get("SUB_DISTRICT_ID")

    result = get_living_env(sub_district_id)
    work_pop = result["work_pop"]
    resident = result["resident"]

    # resident의 비율을 계산
    total_population = work_pop + resident
    resident_percentage = (
        (resident / total_population) * 100 if total_population > 0 else 0
    )
    work_pop_percentage = (
        (work_pop / total_population) * 100 if total_population > 0 else 0
    )
    resident_percentage = int(resident_percentage)
    work_pop_percentage = int(work_pop_percentage)

    # 결과에 resident_percentage 추가
    result["resident_percentage"] = resident_percentage
    result["work_pop_percentage"] = work_pop_percentage

    # print(result)
    return result


def select_statistics_by_sub_district_detail_category(
    city_name: str,
    district_name: str,
    sub_district_name: str,
    biz_detail_category_name: str,
):
    # print(city_name)
    # print(district_name)
    # print(sub_district_name)
    # print(biz_detail_category_name)

    city_id = crud_get_city_id(city_name)
    district_id = crud_get_district_id(city_id, district_name)
    sub_district_id = crud_get_sub_district_id_by(
        city_id, district_id, sub_district_name
    )

    detail_category_id = crud_select_biz_detail_category_id_by_biz_detail_category_name(
        biz_detail_category_name
    )

    # print(city_id)
    # print(district_id)
    # print(sub_district_id)
    # print(detail_category_id)

    stat_item_id_list = []
    stat_item_id_list = crud_select_all_stat_item_id_by_detail_category_id(
        detail_category_id
    )

    statistics_data: CommercialStatisticsData = (
        crud_select_statistics_data_by_sub_district_id_detail_category_id(
            sub_district_id, stat_item_id_list
        )
    )

    # print(statistics_data)

    return statistics_data


def select_statistics_by_store_business_number(
    store_business_number: str,
):
    # print(store_business_number)

    # city_id = crud_get_city_id(city_name)
    # district_id = crud_get_district_id(city_id, district_name)
    # sub_district_id = crud_get_sub_district_id_by(
    #     city_id, district_id, sub_district_name
    # )

    region_id = crud_get_region_id_by_store_business_number(store_business_number)

    print(region_id)

    # detail_category_id = crud_select_biz_detail_category_id_by_biz_detail_category_name(
    #     biz_detail_category_name
    # )

    # print(city_id)
    # print(district_id)
    # print(sub_district_id)
    # print(detail_category_id)

    stat_item_id_list = []
    # stat_item_id_list = crud_select_all_stat_item_id_by_detail_category_id(
    #     detail_category_id
    # )

    # statistics_data: CommercialStatisticsData = (
    #     crud_select_statistics_data_by_sub_district_id_detail_category_id(
    #         sub_district_id, stat_item_id_list
    #     )
    # )

    # print(statistics_data)

    # return statistics_data
    pass
