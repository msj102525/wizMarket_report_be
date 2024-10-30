import os
from app.db.connect import *
import openai
from dotenv import load_dotenv
import openai
from datetime import datetime
from app.schemas.report import GPTAnswerByRisingMenu,LocalStoreTop5Menu 
import logging
from fastapi import HTTPException
from app.crud.gpt_answer import (
    select_region_detail_category_name_by_store_business_number as crud_select_region_detail_category_name_by_store_business_number
)

gpt_content = """
    당신은 전문 조언자입니다. 
    귀하의 역할은 사용자의 질문을 분석하고, 주요 측면을 식별하고, 질문의 맥락을 기반으로 운영 지침과 통찰력을 제공하는 것입니다. 
    접근 방식을 최적화하는 데 도움이 되는 전략이나 솔루션을 제공합니다.
"""

logger = logging.getLogger(__name__)
load_dotenv()
now = datetime.now()
current_time = now.strftime("%Y년 %m월 %d일 %H:%M")
weekday = now.strftime("%A")


# 업종 별 뜨는 메뉴 리포트 생성
def get_gpt_answer_by_rising_business(
    store_business_id: str, rising_menu_top5: LocalStoreTop5Menu 
) -> GPTAnswerByRisingMenu:
    # 상권정보 소분류 카테고리, 지역 동까지, 날짜
    try:
        city_name, district_name, sub_district_name, detail_category_name,  = crud_select_region_detail_category_name_by_store_business_number(store_business_id)
        region_name = f"{city_name} {district_name} {sub_district_name}"
        top_menu_1, top_menu_2, top_menu_3, top_menu_4, top_menu_5 = rising_menu_top5
        # 3. 보낼 프롬프트 설정
        content = f"""
            아래 지역 업종의 뜨는 메뉴가 다음과 같습니다. 
            해당 업종의 매장이 고객을 위해 주요 전략으로 가져가야 할 점이 무엇일지 백종원 쉐프 스타일로 조언을 해주세요.
            단, 말투나 전문적 용어는 점주 성향에 맞추고 조언은 4줄 이하로 해주세요. 

            - 매장 업종 : {detail_category_name}
            - 매장 위치 : {region_name}
            - 뜨는 메뉴 : 1위 {top_menu_1}, 2위 {top_menu_2}, 3위 {top_menu_3}, 4위 {top_menu_4}, 5위 {top_menu_5}
            - 적용날짜 : {current_time}  {weekday} 

        """

        print(content)
        return content
        # openai_api_key = os.getenv("GPT_KEY")
        
        # # OpenAI API 키 설정
        # openai.api_key = openai_api_key

        # completion = openai.chat.completions.create(
        # model="gpt-4o",
        # messages=[
        #     {
        #         "role": "system", 
        #         "content": gpt_content
        #     },
        #     {"role": "user", "content": content}  
        # ]
        # )
        # report = completion.choices[0].message.content

        # return report
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service GPTAnswerByRisingMenu Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Service GPTAnswerByRisingMenu Error: {str(e)}"
        )
            




################ 클로드 결제 후 사용 #################
# import anthropic

# def testCLAUDE():
#     api_key = os.getenv("CLAUDE_KEY")
    
#     # OpenAI API 키 설정
#     openai.api_key = api_key
#     client = anthropic.Anthropic(
#     api_key={api_key},  # 환경 변수를 설정했다면 생략 가능
#     )

#     message = client.messages.create(
#         model="claude-3-opus-20240229",
#         max_tokens=1000,
#         temperature=0.0,
#         system="Respond only in Yoda-speak.",
#         messages=[
#             {"role": "user", "content": "How are you today?"}
#         ]
#     )

#     print(message.content)


############### 라마 ##################
# import ollama

# def testOLLAMA():
#     response = ollama.chat(model='llama3.1:8b', messages=[
#     {
#         'role': 'user',
#         'content': content,
#     },
#     ])
#     print(response['message']['content'])





if __name__ == "__main__":
    get_gpt_answer_by_rising_business("MA0101202212A0017777")