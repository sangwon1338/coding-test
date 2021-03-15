def solution(phone_number):
    last = phone_number[len(phone_number)-4:len(phone_number)]
    num = '*'*(len(phone_number)-4)
    
    return num+last
