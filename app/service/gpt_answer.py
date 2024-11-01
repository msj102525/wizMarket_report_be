import os
from app.db.connect import *
import openai
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
from app.schemas.report import (
    GPTAnswer,
    LocalStoreLocInfoJscoreData,
    LocalStoreTop5Menu,
    LocalStoreRedux,
)
import logging
from fastapi import HTTPException


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


# 뜨는 메뉴 GPT Prompt
def get_rising_business_gpt_answer_by_local_store_top5_menu(
    rising_menu_top5: LocalStoreTop5Menu,
) -> GPTAnswer:

    try:
        city_name = rising_menu_top5.city_name
        district_name = rising_menu_top5.district_name
        sub_district_name = rising_menu_top5.sub_district_name
        detail_category_name = rising_menu_top5.detail_category_name
        region_name = f"{city_name} {district_name} {sub_district_name}"

        top_menu_1 = rising_menu_top5.detail_category_top1_ordered_menu
        top_menu_2 = rising_menu_top5.detail_category_top2_ordered_menu
        top_menu_3 = rising_menu_top5.detail_category_top3_ordered_menu
        top_menu_4 = rising_menu_top5.detail_category_top4_ordered_menu
        top_menu_5 = rising_menu_top5.detail_category_top5_ordered_menu

        content = f"""
            아래 지역 업종의 뜨는 메뉴가 다음과 같습니다. 
            해당 업종의 매장이 고객을 위해 주요 전략으로 가져가야 할 점이 무엇일지 백종원 쉐프 스타일로 조언을 해주세요.
            단, 말투나 전문적 용어는 점주 성향에 맞추고 조언은 4줄 이하로 해주며 <br/>으로 한번씩만 줄바꿈을 해줘. 
            - 매장 업종 : {detail_category_name}
            - 매장 위치 : {region_name}
            - 뜨는 메뉴 : 1위 {top_menu_1}, 2위 {top_menu_2}, 3위 {top_menu_3}, 4위 {top_menu_4}, 5위 {top_menu_5}
            - 적용날짜 : {current_time}  {weekday} 
        """

        # logger.info(f"gpt prompt: {content}")

        client = OpenAI(api_key=os.getenv("GPT_KEY"))
        # OpenAI API 키 설정

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": gpt_content},
                {"role": "user", "content": content},
            ],
        )
        report = completion.choices[0].message.content

        result = GPTAnswer(gpt_answer=report)
        return result

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service GPTAnswer Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service get_rising_business_gpt_answer_by_local_store_top5_menu Error: {str(e)}",
        )


# 입지 정보 J_Score Gpt Prompt
def get_loc_info_gpt_answer_by_local_store_loc_info(
    loc_data=LocalStoreLocInfoJscoreData,
) -> GPTAnswer:
    try:
        region_name = f"{loc_data.city_name} {loc_data.district_name} {loc_data.sub_district_name}"

        # 보낼 프롬프트 설정
        content = f"""
            다음과 같은 매장정보 입지 현황을 바탕으로 매장 입지 특징을 분석하시고 입지에 따른 매장운영 가이드를 제시해주세요. 
            각 항목의 점수는 전체 지역 대비 순위를 나타낸것으로 0~10점으로 구성됩니다.
            단, 말투나 전문적 용어는 점주 성향에 맞추고 조언은 4줄 이하로 해주며, <br/>으로 한번씩만 줄바꿈을 해줘. 
            매장 정보 입지 현황
            - 매장 업종 : {loc_data.detail_category_name}
            - 매장 위치 : {region_name}
            ###########################
            - 위치 : {region_name}
            - 업종 : {loc_data.detail_category_name}
            - 매장이름 : {loc_data.store_name}
            - 화양동 주거인구 수 : 25095명 / 7.8점
            - 화양동 유동인구 수 : 157941명 / 8.4점 
            - 화양동 업소수 : 2265개 / 9.4점
            - 화양동 지역 평균매출 : 41020000원 / 8.2점 ##
            - 화양동 월 평균소비 : 1050000원 / 2.8점  ##
            - 화양동 월 평균소득 : 2220000원 / 0.2점
            - 화양동 세대 수 : 18100개 / 9.6점 ##
            - 화양동 인구 분포 : 10세미만 143명, 10대 392명, 20대 5901명, 30대 2307명, 40대 934명, 50대 873명, 60대 1725 명, 여성 53%, 남성 47% 
        """
        openai_api_key = os.getenv("GPT_KEY")
        # OpenAI API 키 설정
        openai.api_key = openai_api_key
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": gpt_content},
                {"role": "user", "content": content},
            ],
        )
        report = completion.choices[0].message.content
        return report

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service GPTAnswer Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service get_loc_info_gpt_answer_by_local_store_loc_info Error: {str(e)}",
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
    # get_rising_business_gpt_answer_by_local_store_top5_menu("MA0101202212A0017777")

    print("END!!!!!!!!!!!!")
