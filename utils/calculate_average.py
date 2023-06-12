import numpy as np


# 평균 벡터 계산


def cpu_calculate(vectors):
    
    # 벡터들을 NumPy 배열로 변환합니다.
    np_vectors = np.array([vector.numpy() for vector in vectors])

    # 평균을 계산합니다.
    average_vector = np.mean(np_vectors, axis=0)

    return average_vector

# average_vectors = calculate_average(top_corpus_vector)



def gpu_calculate(vectors):
    
    # 벡터들을 GPU로 이동시킵니다.
    gpu_vectors = [vector.to('cuda') for vector in vectors]

    # GPU 상의 벡터들을 NumPy 배열로 변환합니다.
    np_vectors = np.array([vector.cpu().numpy() for vector in gpu_vectors])

    # 평균을 계산합니다.
    average_vector = np.mean(np_vectors, axis=0)

    return average_vector