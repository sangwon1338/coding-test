def solution(a, b):
    answer = ''
    week={1:'FRI',2:'SAT',3:'SUN',4:'MON',5:'TUE',6:'WED',0:'THU'}
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=sum(month[0:a-1])+b
    while(1):
        day=day%7
        if day<7:
            
            return week[day]
