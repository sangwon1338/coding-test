def solution(s):
    answer = ''
    
    str_list = [ord(x) for x in s]

    str_list.sort(reverse=True)
    
    for i in str_list:
        answer += chr(i)
    return answer
