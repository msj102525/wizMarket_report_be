import logging
import pymysql
from fastapi import HTTPException

from app.db.connect import (
    close_connection,
    close_cursor,
    get_db_connection,
)
from app.schemas.report import (
    LocalStoreCDJSWeightedAverage,
    LocalStoreCommercialDistrictJscoreAverage,
    LocalStoreMainCategoryCount,
)

logger = logging.getLogger(__name__)


def select_c_d_j_score_average_by_store_business_number(
    store_business_id: str,
) -> LocalStoreCDJSWeightedAverage:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        COMMERCIAL_DISTRICT_J_SCORE_AVERAGE
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
                        detail=f"LocalStoreCDJSWeightedAverage {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStoreCDJSWeightedAverage(
                    commercial_district_j_score_average=round(
                        row.get("COMMERCIAL_DISTRICT_J_SCORE_AVERAGE"), 1
                    ),
                )

                # logger.info(f"Result for business ID {store_business_id}: {result}")
                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred in select_c_d_j_score_average_by_store_business_number: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")


def select_c_d_main_category_count_by_store_business_number(
    store_business_id: str,
) -> LocalStoreMainCategoryCount:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        COMMERCIAL_DISTRICT_FOOD_BUSINESS_COUNT,
                        COMMERCIAL_DISTRICT_HEALTHCARE_BUSINESS_COUNT,
                        COMMERCIAL_DISTRICT_EDUCATION_BUSINESS_COUNT,
                        COMMERCIAL_DISTRICT_ENTERTAINMENT_BUSINESS_COUNT,
                        COMMERCIAL_DISTRICT_LIFESTYLE_BUSINESS_COUNT,
                        COMMERCIAL_DISTRICT_RETAIL_BUSINESS_COUNT
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
                        detail=f"LocalStoreMainCategoryCount {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStoreMainCategoryCount(
                    commercial_district_food_business_count=row.get(
                        "COMMERCIAL_DISTRICT_FOOD_BUSINESS_COUNT"
                    ),
                    commercial_district_healthcare_business_count=row.get(
                        "COMMERCIAL_DISTRICT_HEALTHCARE_BUSINESS_COUNT"
                    ),
                    commercial_district_education_business_count=row.get(
                        "COMMERCIAL_DISTRICT_EDUCATION_BUSINESS_COUNT"
                    ),
                    commercial_district_entertainment_business_count=row.get(
                        "COMMERCIAL_DISTRICT_ENTERTAINMENT_BUSINESS_COUNT"
                    ),
                    commercial_district_lifestyle_business_count=row.get(
                        "COMMERCIAL_DISTRICT_LIFESTYLE_BUSINESS_COUNT"
                    ),
                    commercial_district_retail_business_count=row.get(
                        "COMMERCIAL_DISTRICT_RETAIL_BUSINESS_COUNT"
                    ),
                )

                logger.info(f"Result for business ID {store_business_id}: {result}")

                # logger.info(f"Result for business ID {store_business_id}: {result}")
                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred in select_c_d_main_category_count_by_store_business_number: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")


def select_commercial_district_j_score_by_store_business_number(
    store_business_id: str,
) -> LocalStoreCommercialDistrictJscoreAverage:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        COMMERCIAL_DISTRICT_MARKET_SIZE_J_SCORE,
                        COMMERCIAL_DISTRICT_AVERAGE_SALES_J_SCORE,
                        COMMERCIAL_DISTRICT_USAGE_COUNT_J_SCORE,
                        COMMERCIAL_DISTRICT_SUB_DISTRICT_DENSITY_J_SCORE,
                        COMMERCIAL_DISTRICT_AVERAGE_PAYMENT_J_SCORE
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

                print(row)

                if not row:
                    raise HTTPException(
                        status_code=404,
                        detail=f"LocalStoreCommercialDistrictJscoreAverage {store_business_id}에 해당하는 매장 정보를 찾을 수 없습니다.",
                    )

                result = LocalStoreCommercialDistrictJscoreAverage(
                    commercial_district_market_size_j_socre=round(row.get(
                        "COMMERCIAL_DISTRICT_MARKET_SIZE_J_SCORE"
                    ),1),
                    commercial_district_average_sales_j_socre=round(row.get(
                        "COMMERCIAL_DISTRICT_AVERAGE_SALES_J_SCORE"
                    ),1),
                    commercial_district_usage_count_j_socre=round(row.get(
                        "COMMERCIAL_DISTRICT_USAGE_COUNT_J_SCORE"
                    ),1),
                    commercial_district_sub_district_density_j_socre=round(row.get(
                        "COMMERCIAL_DISTRICT_SUB_DISTRICT_DENSITY_J_SCORE"
                    ),1),
                    commercial_district_sub_average_payment_j_socre=round(row.get(
                        "COMMERCIAL_DISTRICT_AVERAGE_PAYMENT_J_SCORE"
                    ),1),
                )

                # logger.info(f"Result for business ID {store_business_id}: {result}")
                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred in select_commercial_district_j_score_by_store_business_number: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")
