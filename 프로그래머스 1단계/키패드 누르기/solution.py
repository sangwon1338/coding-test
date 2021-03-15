def solution(numbers, hand):
    answer = ''
    left_dis = 0
    right_dis = 0
    left = [1,4,7]
    right = [3,6,9]
    left_loc = 10
    right_loc = 12
    for i in numbers:     
        if i == 0 :
            i = 11
        if i in left:
            answer += 'L'
            left_loc = i
        elif i in right:
            answer += 'R'
            right_loc = i
        else:
            left_dis = cal_distance(left_loc,i)
            right_dis = cal_distance(right_loc,i)

            if left_dis < right_dis:
                answer += 'L'
                left_loc = i
            if left_dis > right_dis:
                answer += 'R'
                right_loc = i
            if left_dis == right_dis:
                if hand == 'left':
                    answer += 'L'
                    left_loc = i
                if hand == 'right':
                    answer += 'R'
                    right_loc = i
        
    return answer

def cal_distance(a,b):
    dis = abs(a-b)
    if dis == 0:
        distance = 0
    if dis == 1:
        distance = 1
    if dis == 2:
        distance = 2
    if dis == 3:
        distance = 1
    if dis>3 and dis % 3 == 0:
        distance = dis // 3
    if dis>3 and dis % 3 != 0:
        distance = (dis // 3) + (dis % 3)
    return distance
