from sentence_transformers import SentenceTransformer, util
import numpy as np
import torch


# gpu 또는 cpu 에 맞는 sentence transformer 불러오기


if torch.cuda.is_available():
    device = torch.device('cuda')
    embedder = SentenceTransformer("jhgan/ko-sroberta-multitask", device='cuda')
else:
    device = torch.device('cpu')
    embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")


# 상위 n 개 기사 출력


def top_sentences(n, product, news ): # 리스트로 받음

    # embedding
    news_embeddings = embedder.encode(news, convert_to_tensor=True)
    query_embedding = embedder.encode(product, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, news_embeddings)[0]
    cos_scores = cos_scores.cpu()
    
    # 기사 개수에 따라 출력
    if len(news) > 10:
        n = 5
        top_results = np.argpartition(-cos_scores, range(n))[0:n]
    else:
        n = n
        top_results = np.argpartition(-cos_scores, range(n))[0:n]

        
    top_news_list = []
    top_news_vector = []
    top_company_list = []

    # 관련 기사 나열
    for idx in top_results[0:n]:

        top_news_list.append(news[idx])#.strip())
        top_news_vector.append(news_embeddings[idx])
        # top_company_list.append(company_list[idx])

    # return top_company_list, top_news_list, top_news_vector, sum(cos_scores)
    return top_news_list, top_news_vector, sum(cos_scores)


# 코사인 유사도가 높은순으로 나열된 임베딩 벡터들이 top_news_vector 로 반환