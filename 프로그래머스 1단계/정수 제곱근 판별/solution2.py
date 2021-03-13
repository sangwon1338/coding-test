def solution(n):
    answer = 0
    n_root = n ** (1/2)
    if n_root == float(int(n_root)):
        answer = (n_root+1) ** 2
    else:
        answer = -1
    return answer
