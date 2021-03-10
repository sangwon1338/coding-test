def solution(nums):
    answer = 0
    num = int(len(nums)/2)
    nums = set(nums)
    if len(nums) > num:
        answer = num
    else:
        answer = len(nums)
    return answer
