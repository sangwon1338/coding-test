def solution(array, commands):
    answer = []
    for c in commands:
        array_1=sorted(array[c[0]-1:c[1]])
        answer.append(array_1[c[2]-1])
        
        
    
    return answer
