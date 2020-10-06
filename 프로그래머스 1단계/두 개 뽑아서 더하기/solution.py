def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            an = numbers[i] + numbers[j]
            if an not in answer:
                answer.append(an)
    
    answer.sort()
            
    return answer
