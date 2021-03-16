def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        a = binarys(a,n)
        b = binarys(b,n)
        y = ''
        
        for i,j in zip(a,b):
            
            if (int(i)==1) or (int(j)==1):
                y = y + '#'
            else:
                y = y + ' '
        answer.append(y)    
    return answer

def binarys(num,n):
    y=''
    while (num>0):
        
       y = str(num%2)+y 
       num//=2
    if len(y)<n:
        y = str(0)*(n-len(y)) +y
    return y
