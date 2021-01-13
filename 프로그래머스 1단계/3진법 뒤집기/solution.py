def solution(n):
    three = []
    count = 0
    answer = 0
    if n == 1 or n ==2:  
        answer = n
    while n > 2:
        
        three.append(n%3)
        n = n//3
        if n < 3:
            three.append(n%3)
        count +=1

    count = len(three) - 1
    for a in three:
        answer += ((3**count)*a)
        count -= 1
    
    
    
    return answer
