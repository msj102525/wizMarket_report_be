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
                    JOIN LOCAL_STORE_CONTENT_IMAGE lsci ON lsci.LOCAL_STORE_CONTENT_ID = ls.LOCAL_STORE_CONTENT_ID
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
                    # 이미지 URL 추가
                    grouped_results[local_store_content_id]["image_urls"].append(
                        row["LOCAL_STORE_CONTENT_IMAGE_URL"]
                    )

                # 결과를 LocalStoreContent 리스트로 변환
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
