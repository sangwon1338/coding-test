def solution(x):
    answer = True
    num = 0
    origin = x
    while (1):
        num += (x % 10)
        x = x // 10     
        if x < 10:
            num += x  
            break
    if origin % num != 0:
        answer = False
    return answer
