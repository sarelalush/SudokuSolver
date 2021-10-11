


def print_board(bo):
    print('-------------------------------------')
    for i in range(1,10):
        if (i-1) % 3 == 0 and i-1 != 0 :
                print('-------------------------------------')
        print("| " , end = "")
        for j in range(1,10):
            if((j-1) % 3 == 0 and j-1 !=0):
                print(" | " ,end='')
            print(f' {bo[i-1][j-1]} ' , end = '')
            if j == 9:
                print(" |" , end = "")
        print()
    print('-------------------------------------')