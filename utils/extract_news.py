from datetime import datetime, timedelta, timezone
from utils import naver_news_api, preprocess_text
# import streamlit as st


# 현재 시각 구하기 (한국 시간대)
current_time = datetime.now(timezone(timedelta(hours=9)))

# 3개월(90일) 이전 시각 계산
three_months_ago = current_time - timedelta(days=90)


# extract_descript 함수 선언

def extract_descript(name):

    json_data = naver_news_api.naver_news(100, name) # news api
    summary_list = []
    cleaned_news = []
    original_news = []
    link_list = []

    for number in range(len(json_data)):
        summary = json_data[number]['description']
        # link = json_data[number]['originallink']
        link = json_data[number]['link']
        
        # 동일 기사 제외
        if summary not in summary_list:
            summary_list.append(summary)
            # if len(set(nltk.word_tokenize(summary) & nltk.word_tokenize(summary_list[number]))) < 7:
#             st.text(summary.split())
#             st.text(number)
#             st.text(summary_list[number].split())
            
#             for check in summary_list:
#                 if len(set(summary.split()) & set(summary_list[number].split())) < 7:
            
            # 기업이름 포함 기사 추출
            if name in summary:

                # 3개월 이내 기사
                if datetime.strptime(json_data[number]['pubDate'], '%a, %d %b %Y %H:%M:%S %z').replace(tzinfo=timezone(timedelta(hours=9))) >= three_months_ago:

                    # 전처리
                    cleaned_summary = preprocess_text.preprocess(summary)
                    original_summary = preprocess_text.preprocess_unescape(summary)
                    cleaned_news.append(cleaned_summary)
                    original_news.append(original_summary)
                    link_list.append(link)

    return cleaned_news, original_news, link_list
