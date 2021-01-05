def solution(board, moves):
    answer = 0
    re = []

    for i in range(len(moves)):
        k=moves[i]-1

        for j in range(len(board)):
            
            if board[j][k] !=0:

                
                if len(re) == 0:

                    re.append(board[j][k])
                    
                    board[j][k]=0

                else:
                    
                    
                     if re[-1] == board[j][k]:
                        re.pop()
                        
                        answer +=2
                    
                        board[j][k]=0
                    
                     else:
                        
                        re.append(board[j][k])
                        board[j][k]=0
                
                break

    return answer
