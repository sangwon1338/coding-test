def solution(n, m):
    answer = []
    min_n = min(n,m)
    max_n = max(n,m)
    #  최대 공약수
    for i in range(1,max_n+1):
        if (n%i==0) and (m%i==0):
            temp = i

    answer.append(temp)
    #  최소 공배수
    for i in range(max_n,n*m+1):
        if i%n==0 and i%m==0:
            temp = i
            break
    answer.append(temp)
    return answer
