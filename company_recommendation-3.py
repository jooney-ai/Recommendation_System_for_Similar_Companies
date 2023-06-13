from utils import info, top_news, product_token, delete, newline
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime, timedelta, timezone
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from tqdm.notebook import tqdm
import dart_fss as dart
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import torch
# import nltk
import json
import re

    

# api key 설정, 회사 리스트 불러오기

KOSPI, corp_list = info.dart_api()


# 웹사이트에 데이터 저장

@st.cache_data
def load_data():
    return info.load(KOSPI)
data = load_data()


###########################################################################################


# streamlit


product = st.text_input('사업내용을 입력해 주세요')
keyword_text = st.text_input('사업내용의 핵심 키워드를 입력해 주세요')
keyword_list = keyword_text.split(',')
key_tokens = [ keyword.replace(' ', '') for keyword in keyword_list ]
confirm = st.button("Confirm")


if confirm:          

    company_list, top_content, top_original, link_list = product_token.top_token(data, key_tokens)
    score_list = []

    for company, news_list, original_news_list, link in zip(company_list, top_content, top_original, link_list):

        top_news_list, top_news_vector, cos_scores = top_news.top_sentences(len(news_list), product, news_list)
        score_list.append((company, cos_scores, top_news_list, original_news_list, link))

    rank = sorted(score_list, key=lambda x: x[1], reverse=True)[:5] # 회사, 점수, 상위뉴스, 기존뉴스, 링크
        
    # rank 정보를 파일로 저장
    
    save_data = rank
    pd.DataFrame(save_data).to_csv('data.csv', index = False)
    

df = pd.read_csv('data.csv', encoding='utf-8')

first_company = df.iloc[0,:]
second_company = df.iloc[1,:]
third_company = df.iloc[2,:]

rank = [first_company,second_company,third_company]


# 회사 선택
    
newline.enter(3, sidebar=False)
choose_company = st.radio('확인하고 싶은 회사를 선택하세요', (first_company[0], second_company[0], third_company[0]))
newline.enter(3, sidebar=False)

first_company = first_company[0]
if choose_company == first_company:
    info.get_info(data, rank[0], first_company, corp_list)   
    
elif choose_company == second_company[0]:
    info.get_info(data, rank[1], second_company[0], corp_list)   
    
elif choose_company == third_company[0]:
    info.get_info(data, rank[2], third_company[0], corp_list)   


# 워터마크 삭제

delete.watermark()


# else:
#     st.subheader('검색결과가 없습니다')
