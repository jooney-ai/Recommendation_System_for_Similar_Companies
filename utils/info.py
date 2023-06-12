from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from utils import newline, extract_news
import dart_fss as dart
import streamlit as st


def load(KOSPI):
    
    data = {}

    for company_info in KOSPI:
        # st.progress(company_info)
        # do_something_slow()
        company = company_info.corp_name

        if company not in ['대동','유니온','동양','한창','대현','서연이화','금비','방림']:
            data[company] = {}
            data[company]['news'] = {}
            news = data[company]['news']
            news['cleaned_news'], news['original_news'], news['link'] = extract_news.extract_descript(company) # 전처리 뉴스, 기존 뉴스, 링크
            data[company]['sector'] = company_info.sector
            data[company]['product'] = company_info.product
    
    return data


def get_info(data, rank, company, corp_list):
    
    st.title('기업 추천 (Prototype)')
    newline.enter(4, sidebar=False)
    
    # company_report = corp_list.find_by_corp_name(company, market='Y', exactly=True)[0]
    with st.sidebar:
        choose = option_menu("추천 회사", ["기업 정보", "최근 뉴스"],
                             icons=['book', 'activity'],
                             menu_icon="app", default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )
    
    if choose == "기업 정보":
    
             


        st.header(f'기업 이름 : {company}')

        st.divider()
        st.subheader('')
        st.subheader(data[company]['sector'])
        st.markdown('')
        st.markdown(data[company]['product'])
        st.markdown('')
        st.divider()
        
        
        report = corp_list.find_by_corp_name(company, market='Y', exactly=True)[0].search_filings(bgn_de='20230101')

        for i, item in enumerate(report.to_dict()['report_list']):
            # st.text(i)
            # st.text(item)

            if '분기보고서' in item['report_nm']:
                idx = i

        # 사업의 개요

        newline.enter(2, sidebar=False)

        st.divider()
        st.subheader('사업의 개요')
        st.divider()
        st.text('')
        summary = report[idx][9]
        components.html(summary.html, width=800, height=500, scrolling=True)


        # 주요 제품 및 서비스

        newline.enter(8, sidebar=False)

        st.divider()
        st.subheader('주요 제품 및 서비스')
        st.divider()
        st.text('')
        main_product = report[idx][10]
        components.html(main_product.html, width=800, height=600, scrolling=True)


    # News

    elif choose == "최근 뉴스":
        st.subheader('News')

        st.text('')
    #     st.markdown(rank[0][3][0])
    #     st.info(rank[0][4][0])
    #     st.markdown(rank[0][3][1])
    #     st.info(rank[0][4][1])
    #     st.markdown(rank[0][3][2])
    #     st.info(rank[0][4][2])

        st.markdown(eval(rank[3])[0])
        st.info(eval(rank[4])[0])
        st.markdown(eval(rank[3])[1])
        st.info(eval(rank[4])[1])
        st.markdown(eval(rank[3])[2])
        st.info(eval(rank[4])[2])


        # 분기보고서 페이지


    
    
    
    
def dart_api():
    
    api_key='c9670528b4f198d08f0f07a54c550935aaa5bafb'
    dart.set_api_key(api_key=api_key)
    corp_list = dart.get_corp_list()
    KOSPI = corp_list.find_by_corp_name('', market='Y')
    
    return KOSPI, corp_list