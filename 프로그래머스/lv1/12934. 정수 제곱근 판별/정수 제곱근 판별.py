import numpy as np

def solution(n):
    if np.sqrt(n) % 1 == 0:
        answer = (np.sqrt(n) + 1) ** 2
    else:
        answer = -1
    return answer