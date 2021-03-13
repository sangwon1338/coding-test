import math
def solution(n):
    answer = 0
    n_root = math.sqrt(n)
    print(type(n_root))
    if n_root == float(int(n_root)):
        answer = math.pow(n_root+1,2)
    else:
        answer = -1
    return answer
