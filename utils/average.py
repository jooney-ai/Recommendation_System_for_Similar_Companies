
def vector(company_name, product):

    news = []
    company_name = "퓨쳐스콜레" # 검색 할 수 있도록
    json_data = naver_news_api.naver_news(100, company_name)

    for number in range(len(json_data)):

        summary = json_data[number]['description']
        cleaned_summary = preprocess_text.preprocess(summary)

        # '기업이름 포함 기사만 추출'
        if company_name in cleaned_summary:
            news.append(cleaned_summary)
        # 3개월 이내 추가

    # 퓨쳐스콜레 평균벡터

    product = ['서비스 교육서비스업 소프트웨어개발 온라인정보제공업 온라인교육']

    top_corpus, top_corpus_vector = top_news.top_sentences(5, product, news)
    future_average_vector = calculate_average.calculate(top_corpus_vector)

return news, future_average_vector