import urllib.request
import json



# 네이버 검색 API Key

client_id = "4I9k6DtOYxCPGKPnE6Hq"
client_secret = "QwAEPvI1k1"

display = 100 # 키워드 당 검색해서 저장할 기사 수



def naver_news(display, company_name):
        
    display = display
    encText = urllib.parse.quote(company_name)

    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + \
            "&display=" + str(display) + "&sort=date" # JSON 결과 (뉴스) # + "&sort=sim"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        decoded_data = response_body.decode('utf-8')
        json_data = json.loads(decoded_data)
        return json_data['items']
        
    else:
        print("Error Code:" + rescode)