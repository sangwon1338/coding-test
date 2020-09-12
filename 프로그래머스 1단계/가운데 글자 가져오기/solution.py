def solution(s):
    answer = ''
    length=len(s)
    mid=int(length/2)
    if (length%2)==0:
        
        answer=s[mid-1]+s[mid]
    else:
        answer=s[mid]
    return answer
