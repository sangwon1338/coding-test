def solution(N, stages):
    answer = []
    
    a = {}
    length = len(stages)
    for i in range(1,N+1):
        if length == 0:
            a[i] = 0
            continue
        a[i] = stages.count(i)/length
        length -= stages.count(i)
         
    answers = sorted(a.items(),reverse=True,key=lambda item: item[1])
    
    answer = [answers[i][0] for i in range(len(answers))]

    return answer
