import os
from app.db.connect import *
import openai
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
from app.schemas.report import (
    GPTAnswer,
    LocalStoreLocInfoJscoreData,
    LocalStoreRisingBusinessNTop5SDTop3,
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
            단, 말투나 전문적 용어는 점주 성향에 맞추고 조언은 4줄 이하로 해주며 두번째줄부터 <br/>으로 한번씩만 줄바꿈을 해줘. 
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
            단, 말투나 전문적 용어는 점주 성향에 맞추고 조언은 4줄 이하로 해주며, 두번째줄부터 <br/>으로 한번씩만 줄바꿈을 해줘. 
            매장 정보 입지 현황
            - 매장 업종 : {loc_data.detail_category_name}
            - 매장 위치 : {region_name}
            ###########################
            - 위치 : {region_name}
            - 업종 : {loc_data.detail_category_name}
            - 매장이름 : {loc_data.store_name}
            - 화양동 주거인구 수 : {(loc_data.loc_info_resident_k) * 1000} / {loc_data.loc_info_resident_j_score}점
            - 화양동 유동인구 수 :  {(loc_data.loc_info_move_pop_k) * 1000} / {loc_data.loc_info_move_pop_j_score}점
            - 화양동 업소수 :{(loc_data.loc_info_shop_k) * 1000} / {loc_data.loc_info_shop_j_score}점
            - 화양동 지역 평균매출 : {(loc_data.loc_info_average_sales_k) * 1000} / {loc_data.loc_info_average_sales_j_score}점
            - 화양동 월 평균소비 :  {(loc_data.loc_info_average_spend_k) * 1000} / {loc_data.loc_info_average_spend_j_score}점
            - 화양동 월 평균소득 :  {(loc_data.loc_info_income_won) * 10000} / {loc_data.loc_info_income_j_score}점
            - 화양동 세대 수 :  {(loc_data.loc_info_house_k) * 1000} / {loc_data.loc_info_house_j_score}점
            - 화양동 인구 분포 : 10세미만 {loc_data.population_age_10_under}명, 10대 {loc_data.population_age_10s}명, 20대 {loc_data.population_age_20s}명, 30대 {loc_data.population_age_30s}명, 40대 {loc_data.population_age_40s}명, 50대 {loc_data.population_age_50s}명, 60대 {loc_data.population_age_60_over}명, 여성 {round(loc_data.population_female_percent, 1) or 0}% , 남성 {round(loc_data.population_male_percent, 1) or 0}% 

        """
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

        # logger.info(f"loc_info_prompt: {content}")
        # logger.info(f"loc_info_gpt: {report}")

        result = GPTAnswer(gpt_answer=report)
        return result

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service GPTAnswer Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service get_loc_info_gpt_answer_by_local_store_loc_info Error: {str(e)}",
        )


# 상권분석 J_Score Gpt Prompt
def get_loc_info_gpt_answer_by_local_store_commercial_district(
    loc_data=LocalStoreLocInfoJscoreData,
) -> GPTAnswer:
    try:
        region_name = f"{loc_data.city_name} {loc_data.district_name} {loc_data.sub_district_name}"

        # 보낼 프롬프트 설정
        content = f"""

        """
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

        # logger.info(f"loc_info_prompt: {content}")
        # logger.info(f"loc_info_gpt: {report}")

        result = GPTAnswer(gpt_answer=report)
        return result

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service GPTAnswer Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service get_loc_info_gpt_answer_by_local_store_commercial_district Error: {str(e)}",
        )


# 뜨는업종 Gpt Prompt
def get_loc_info_gpt_answer_by_local_store_rising_business(
    rising_data=LocalStoreRisingBusinessNTop5SDTop3,
) -> GPTAnswer:
    try:

        # 보낼 프롬프트 설정
        content = f"""
                2024년 8월
                전국 매출 증가 업종 TOP5 
                1위 : 경상남도	통영시 북신동	소매/유통	인테리어/소품	보일러/냉난방용품  22911.8%
                2위 : 인천광역시	미추홀구	도화1동	소매/유통	인테리어/소품 보일러/냉난방용품 21067.5%
                3위 : 부산광역시	금정구	서3동	소매/유통	패션잡화	구두제화/캐주얼화 11598.3%
                4위 : 경기도	안양시	관양동	소매/유통	가전제품	이동통신기기 10410.2%
                5위 : 부산광역시	강서구	녹산동	음식	양식	정통양식/경양식  7172.1%
                당산2동 매출 증가 업종 Top3
                1위 : 음식	간이주점	이자까야	904.8%
                2위 : 학문/교육	독서실/고시원	독서실/장소대여	127.1%
                3위 : 소매/유통	패션잡화	잡화점	57% 
                위 정보를 바탕으로 당산2동에서 돼지고기 구이 찜 업종 매장인 '일차3.5숙성고기' 점포의 영업전략 분석과 조언을 해주세요. 
        """
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

        # logger.info(f"loc_info_prompt: {content}")
        # logger.info(f"loc_info_gpt: {report}")

        result = GPTAnswer(gpt_answer=report)
        return result

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Service GPTAnswer Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Service get_loc_info_gpt_answer_by_local_store_rising_business Error: {str(e)}",
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
