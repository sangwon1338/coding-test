def solution(arr):
    answer = []
    if arr == [10] or arr == []:
        answer.append(-1)
    else:
        arr.remove((min(arr)))
        answer = arr
        
    return answer
