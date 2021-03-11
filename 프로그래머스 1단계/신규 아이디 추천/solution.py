second = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_','.']

def solution(new_id):
    #1단계
    new_id = new_id.lower()
    
    #2단계
    list(new_id)
    new_ids = []
    for i in new_id:
        if i in second:
            new_ids.append(i)
    new_id = []
    old = ''
    
    #3단계
    for i in range(len(new_ids)):
        if i == 0:
            new_id.append(new_ids[i])
        if i>0 and new_ids[i] != '.':
            new_id.append(new_ids[i])
        if i > 0 and new_ids[i] == '.':
            if new_ids[i-1] == new_ids[i]:
                continue
            else:
                new_id.append(new_ids[i])
    
    #4단계
    if len(new_id) == 1:
        if new_id[0] == '.':
            del new_id[0]
    if len(new_id) > 1:
        if new_id[0] == '.':
            del new_id[0]
        if new_id[-1] == '.':
            del new_id[-1]
    

    #5단계
    if len(new_id) == 0:
        new_id.append('a')
    
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            del new_id[-1]
            
    #7단계
    while (len(new_id)<=2):
        new_id.append(new_id[-1])
    
        
    
    answer = ''.join(new_id)
    return answer
