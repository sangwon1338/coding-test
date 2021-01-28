def solution(n):
    answer = ''
    for i in range(int(n/2)):
        
        answer += '수박'
    if n%2 == 1:
        answer += '수'
    if n == 1 :
        answer = '수'

            
    return answer
