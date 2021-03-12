def solution(n):
    answer = ''
    n = str(n)
    k = []
    for i in range(len(n)):
        k.append(int(n[i]))
    k.sort(reverse=True)
    for i in range(len(k)):
        answer += str(k[i])
  
    return int(answer)
