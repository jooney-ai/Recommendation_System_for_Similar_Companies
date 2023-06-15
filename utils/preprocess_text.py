import html
import re


def preprocess(text):

    # 태그 제거, unescape
    pattern = re.compile(r'<.*?>')
    text = re.sub(pattern, '', text)
    text = html.unescape(text)
    text = re.sub(r"[^가-힣a-zA-Z\s]", "", text)

    # 토큰화
    tokens = text.split()
    
    # 불용어 제거
    # stop_words = set(stopwords.words('korean'))  # 불용어 목록은 해당 언어에 맞게 설정
    # tokens = [token for token in tokens if token not in stop_words]

    # 형태소 분석기로 토큰화
    # tokenizer = Mecab()
    # tokens = tokenizer.morphs(text)
    
    # 한국어 불용어 제거
    # stop_words = set(stopwords.words('korean'))
    # tokens = [token for token in tokens if token not in stop_words]

    
    # 어근 추출 또는 표제어 추출
    tokens = [ token for token in tokens if len(token) > 1 ]
    # tokens = [token for token in tokens if len(token) > 1]
    
    # 정규화
    # 추가적인 정규화 작업이 필요하다면 해당 작업을 수행
    
    # 전처리된 텍스트 반환
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text


def preprocess_unescape(text):

    # 태그 제거, unescape
    pattern = re.compile(r'<.*?>')
    text = re.sub(pattern, '', text)
    text = html.unescape(text)

    # 토큰화
    tokens = text.split()
    
    # 어근 추출 또는 표제어 추출
    tokens = [ token for token in tokens if len(token) > 1 ]

    # 전처리된 텍스트 반환
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text
