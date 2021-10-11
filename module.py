
def back_track_solver(board):
    
    pos = get_empty_pos(board)
    #if pos is None we Finish
    if pos == None:
        return True

    for i in range(1,10):
        if checkValid(board,i,pos):
            board[pos[0]][pos[1]] = i
            #go to the next pos
            if back_track_solver(board):
                return True
        #go back and try again with higher number     
        #we need to set this pos to zero
        #if we dont do it the function checkValid will not work 
        board[pos[0]][pos[1]] = 0
    return False
                
#find the next pos with zero
def get_empty_pos(board):
    length = len(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None
    
def checkValid(board , num , pos):
    #check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    #check the colunm
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check the Frame
    _x = pos[1] // 3
    _y = pos[0] // 3

    for i in range(_y*3 , _y+3):
        for j in range(_x*3 , _x*3 +3):
            if board[i][j] == num and pos != (i,j) :
                return False
    #valid pos
    return True

def print_board(board):
    print('-------------------------------------')
    for i in range(1,10):
        if (i-1) % 3 == 0 and i-1 != 0 :
                print('-------------------------------------')
        print("| " , end = "")
        for j in range(1,10):
            if((j-1) % 3 == 0 and j-1 !=0):
                print(" | " ,end='')
            print(f' {board[i-1][j-1]} ' , end = '')
            if j == 9:
                print(" |" , end = "")
        print()
    print('-------------------------------------')