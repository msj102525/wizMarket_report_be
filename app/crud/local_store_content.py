import logging
from typing import List
import pymysql
from fastapi import HTTPException

from app.db.connect import (
    close_connection,
    close_cursor,
    get_db_connection,
)
from app.schemas.report import (
    BizDetailCategoryContent,
    LocalStoreContent,
)

logger = logging.getLogger(__name__)


def select_local_store_content_by_store_business_number(
    store_business_id: str,
) -> List[LocalStoreContent]:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT 
                        ls.LOCAL_STORE_CONTENT_ID,
                        ls.TITLE,
                        ls.CONTENT,
                        lsci.LOCAL_STORE_CONTENT_IMAGE_URL
                    FROM
                        LOCAL_STORE_CONTENT ls
                    LEFT JOIN LOCAL_STORE_CONTENT_IMAGE lsci ON lsci.LOCAL_STORE_CONTENT_ID = ls.LOCAL_STORE_CONTENT_ID
                    WHERE STORE_BUSINESS_NUMBER = %s
                    AND ls.STATUS != 'D'
                    ;
                """

                cursor.execute(select_query, (store_business_id,))
                rows = cursor.fetchall()

                if not rows:
                    return []

                grouped_results = {}

                for row in rows:
                    local_store_content_id = row["LOCAL_STORE_CONTENT_ID"]
                    if local_store_content_id not in grouped_results:
                        grouped_results[local_store_content_id] = {
                            "title": row["TITLE"],
                            "content": row["CONTENT"],
                            "image_urls": [],
                        }
                    grouped_results[local_store_content_id]["image_urls"].append(
                        row["LOCAL_STORE_CONTENT_IMAGE_URL"]
                    )

                result = [
                    LocalStoreContent(
                        local_store_content_id=local_store_content_id,
                        store_description_title=data["title"],
                        store_description_content=data["content"],
                        store_description_img_url=data["image_urls"],
                    )
                    for local_store_content_id, data in grouped_results.items()
                ]

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred in select_local_store_content_by_store_business_number: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")


def select_biz_detail_category_id_list_by_store_business_number(
    store_business_id: str,
) -> List[int]:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                select_query = """
                    SELECT
                        R.BUSINESS_AREA_CATEGORY_ID,
                        DCM.DETAIL_CATEGORY_ID
                    FROM
                        REPORT R
                    JOIN DETAIL_CATEGORY_MAPPING DCM ON DCM.BUSINESS_AREA_CATEGORY_ID = R.BUSINESS_AREA_CATEGORY_ID
                    WHERE
                        STORE_BUSINESS_NUMBER = %s
                    ;
                """

                cursor.execute(select_query, (store_business_id,))
                rows = cursor.fetchall()

                # logger.info(f"rows: {rows}")

                result = []

                for row in rows:
                    result.append(row["DETAIL_CATEGORY_ID"])

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred in select_biz_detail_category_id_list_by_store_business_number: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")


def select_detail_category_content_by_biz_detail_category_id_list(
    detail_category_id_list: List[int],
) -> List[BizDetailCategoryContent]:

    try:
        with get_db_connection() as connection:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                detail_category_ids = ",".join(map(str, detail_category_id_list))

                select_query = f"""
                    SELECT 
                        BDCC.BIZ_DETAIL_CATEGORY_CONTENT_ID,
                        BDCC.TITLE,
                        BDCC.CONTENT,
                        BDCCI.BIZ_DETAIL_CATEGORY_CONTENT_IMAGE_URL
                    FROM
                        BIZ_DETAIL_CATEGORY_CONTENT BDCC
                    LEFT JOIN BIZ_DETAIL_CATEGORY_CONTENT_IMAGE BDCCI 
                        ON BDCCI.BIZ_DETAIL_CATEGORY_CONTENT_ID = BDCC.BIZ_DETAIL_CATEGORY_CONTENT_ID
                    WHERE 
                        BDCC.DETAIL_CATEGORY_ID IN ({detail_category_ids})
                        AND BDCC.STATUS != 'D'
                    ;
                """

                cursor.execute(select_query)
                rows = cursor.fetchall()

                if not rows:
                    return []

                grouped_results = {}

                for row in rows:
                    biz_detail_category_content_id = row[
                        "BIZ_DETAIL_CATEGORY_CONTENT_ID"
                    ]
                    if biz_detail_category_content_id not in grouped_results:
                        grouped_results[biz_detail_category_content_id] = {
                            "title": row["TITLE"],
                            "content": row["CONTENT"],
                            "image_urls": [],
                        }
                    grouped_results[biz_detail_category_content_id][
                        "image_urls"
                    ].append(row["BIZ_DETAIL_CATEGORY_CONTENT_IMAGE_URL"])

                result = [
                    BizDetailCategoryContent(
                        biz_detail_category_content_id=biz_detail_category_content_id,
                        detail_category_description_title=data["title"],
                        detail_category_description_content=data["content"],
                        detail_category_description_img_url=data["image_urls"],
                    )
                    for biz_detail_category_content_id, data in grouped_results.items()
                ]

                return result

    except pymysql.Error as e:
        logger.error(f"Database error occurred: {str(e)}")
        raise HTTPException(status_code=503, detail=f"데이터베이스 연결 오류: {str(e)}")
    except Exception as e:
        logger.error(
            f"Unexpected error occurred in select_detail_category_content_by_biz_detail_category_id_list: {str(e)}"
        )
        raise HTTPException(status_code=500, detail=f"내부 서버 오류: {str(e)}")
