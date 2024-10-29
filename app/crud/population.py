import logging
import pymysql
from fastapi import HTTPException

from app.db.connect import (
    close_connection,
    close_cursor,
    get_db_connection,
)
from app.schemas.report import (
    LocalStorePopulationDataOutPut,
)

logger = logging.getLogger(__name__)


def select_population_by_store_business_number(
    store_business_id: str,
) -> LocalStorePopulationDataOutPut:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        POPULATION_TOTAL,
                        POPULATION_MALE_PERCENT,
                        POPULATION_FEMALE_PERCENT,
                        POPULATION_AGE_10_UNDER,
                        POPULATION_AGE_10S,
                        POPULATION_AGE_20S,
                        POPULATION_AGE_30S,
                        POPULATION_AGE_40S,
                        POPULATION_AGE_50S,
                        POPULATION_AGE_60_OVER,
                        LOC_INFO_RESIDENT_K,
                        LOC_INFO_WORK_POP_K,
                        LOC_INFO_MOVE_POP_K,
                        LOC_INFO_SHOP_K,
                        LOC_INFO_INCOME_WON,
                        LOC_INFO_RESIDENT_J_SCORE,
                        LOC_INFO_WORK_POP_J_SCORE,
                        LOC_INFO_MOVE_POP_J_SCORE,
                        LOC_INFO_SHOP_J_SCORE,
                        LOC_INFO_INCOME_J_SCORE
                    FROM
                        REPORT 
                    WHERE STORE_BUSINESS_NUMBER = %s
                    ;
                """

                # logger.info(
                #     f"Executing query: {select_query} with business ID: {store_business_id}"
                # )
                cursor.execute(select_query, (store_business_id,))

                row = cursor.fetchone()

                if not row:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStorePopulationDataOutPut {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStorePopulationDataOutPut(
                    population_total=row.get("POPULATION_TOTAL"),
                    population_male_percent=row.get("POPULATION_MALE_PERCENT"),
                    population_female_percent=row.get("POPULATION_FEMALE_PERCENT"),
                    population_age_10_under=row.get("POPULATION_AGE_10_UNDER"),
                    population_age_10s=row.get("POPULATION_AGE_10S"),
                    population_age_20s=row.get("POPULATION_AGE_20S"),
                    population_age_30s=row.get("POPULATION_AGE_30S"),
                    population_age_40s=row.get("POPULATION_AGE_40S"),
                    population_age_50s=row.get("POPULATION_AGE_50S"),
                    population_age_60_over=row.get("POPULATION_AGE_60_OVER"),
                    loc_info_resident_k=row.get("LOC_INFO_RESIDENT_K"),
                    loc_info_work_pop_k=row.get("LOC_INFO_WORK_POP_K"),
                    loc_info_move_pop_k=row.get("LOC_INFO_MOVE_POP_K"),
                    loc_info_shop_k=row.get("LOC_INFO_SHOP_K"),
                    loc_info_income_won=row.get("LOC_INFO_INCOME_WON"),
                    loc_info_resident_j_score=round(
                        row.get("LOC_INFO_RESIDENT_J_SCORE"), 1
                    ),
                    loc_info_work_pop_j_score=round(
                        row.get("LOC_INFO_WORK_POP_J_SCORE"), 1
                    ),
                    loc_info_move_pop_j_score=round(
                        row.get("LOC_INFO_MOVE_POP_J_SCORE"), 1
                    ),
                    loc_info_shop_j_score=round(row.get("LOC_INFO_SHOP_J_SCORE"), 1),
                    loc_info_income_j_score=round(row.get("LOC_INFO_INCOME_J_SCORE"), 1),
                )

                logger.info(f"Result for business ID {store_business_id}: {result}")
                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred in select_population_by_store_business_number: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")
