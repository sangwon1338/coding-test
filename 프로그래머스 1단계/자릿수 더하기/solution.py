def solution(n):
    answer = 0

        
    while True:
        answer += (n%10)
        if n < 10:
            break
        
        n = n//10

    return answer
