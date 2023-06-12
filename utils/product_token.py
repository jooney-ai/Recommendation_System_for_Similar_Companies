





# def top_token(dic, company_description_list, key_tokens):
def top_token(dic, key_tokens):
    
    # content = []
    count_sum = []
    
    for company in dic:
        
        sameword_info = []
        news = dic[company]['news']
        
        # 한 기업에서 포함단어 개수를 상위권으로 나열하고
        for cleaned_news, original_news, link in zip(news['cleaned_news'], news['original_news'], news['link']):
        # for idx, news_list in enumerate(company_description_list):


        # '한 기업당'
        # for description in news:

            sameword_list = [] # 포함단어 리스트

            # '기업내용 토큰중 얼마나 포함되어 있는지'
            for keywords in key_tokens:
                if keywords in cleaned_news.replace(' ', ''):
                    sameword_list.append(keywords)

            # '요약기사, 포함단어 수, 포함단어 목록'
            result = (cleaned_news, original_news, link, len(sameword_list), sameword_list)
            sameword_info.append(result)

            # '포함단어 개수 순으로 나열'
        results = sorted(sameword_info, key=lambda x: x[3], reverse=True)

        # '상위 10 개 기사'
        count_list = []
        cleaned_news_list = []
        original_news_list = []
        link_list = []
        for result in results[:10]:
            cleaned_news, original_news, link, count, sameword_list = result
            count_list.append(count)
            cleaned_news_list.append(cleaned_news)
            original_news_list.append(original_news)
            link_list.append(link)

        # content.append(description_list)

        # 포함단어 총합개수
        # count_sum.append((company, idx, sum(count_list)))
        count_sum.append((company, cleaned_news_list, original_news_list, link_list, sum(count_list)))

    # 상위 20개 기업
    rank = sorted(count_sum, key=lambda x: x[-1], reverse=True)[:20]
    # idx_list = [ idx[0] for idx in rank ]

    top_company_list = [ top_company[0] for top_company in rank ]
    top_content = [ top_content[1] for top_content in rank ]
    top_original = [ top_content[2] for top_content in rank ]
    link = [ top_content[3] for top_content in rank ]
    
    # top_content = [ content[i] for i in idx_list ]
    
    return top_company_list, top_content, top_original, link