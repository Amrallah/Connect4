import numpy as np
rowsNo=6
columnsNo=7

board=np.zeros((rowsNo,columnsNo))
print (board)

def selectColumn(player):
    if player%2!=0:
        pieceLocation = input("Player 1, in which column you want to place your piece?")
        i = 1
        while (board[rowsNo - i][int(pieceLocation) - 1] != 0):
            i += 1
        board[rowsNo - i][int(pieceLocation) - 1] = 1
    elif player%2==0:
        pieceLocation = input("Player 2, in which column you want to place your piece?")
        i = 1
        while (board[rowsNo - i][int(pieceLocation) - 1] != 0):
            i += 1
        board[rowsNo - i][int(pieceLocation) - 1] = 2

        
def dropPiece(boardC,pieceLocation):
    i=1
    while(boardC[rowsNo-i][int(pieceLocation)]!=0):
        i+=1
    boardC[rowsNo - i][int(pieceLocation)] = 2
        
def newBoards(board):
    listNewBoards=[]
    for i in range(columnsNo):
        if(validColumn(board,i) == True ):
            boardI=board.copy()
            dropPiece(boardI,i)
           #print(boardI)
            listNewBoards.append(boardI)
            
    #print (listNewBoards)
    return listNewBoards
    

def horizontalWin(array):
    horizontal_flag_1=0
    horizontal_flag_2=0
    transposed=array.T
    for i in range(rowsNo):
        for r in range(columnsNo):
            if transposed[r][i]==1:
                horizontal_flag_1+=1
                if horizontal_flag_1==4:
                    print("Player 1 wins")
                    break
            else:
                horizontal_flag_1=0
            if transposed[r][i]==2:
                horizontal_flag_2+=1
                if horizontal_flag_2==4:
                    print("Player 2 wins")
                    break
            else:
                horizontal_flag_2=0
        if horizontal_flag_1==4:
        	horizontal_flag_1=0
        	break
        elif horizontal_flag_2==4:
            horizontal_flag_2=0
            break
    return

def verticalWin(array):
    vertical_flag_1=0
    vertical_flag_2=0
    for i in range(columnsNo):
        for r in range(rowsNo):
            if array[r][i]==1:
                vertical_flag_1+=1
                if vertical_flag_1==4:
                    print("Player 1 wins")
                    break
            else:
                vertical_flag_1=0
            if array[r][i]==2:
                vertical_flag_2+=1
                if vertical_flag_2==4:
                    print("Player 2 wins")
                    break
            else:
                vertical_flag_2=0
        if vertical_flag_1==4:
        	vertical_flag_1=0
        	break
        elif vertical_flag_2==4:
            vertical_flag_2=0
            break
    return

def negativeDiagonalWin(array):
    win=False
    for i in range(columnsNo-3):
        for r in range(rowsNo-3):
            if array[r][i]==1 and array[r+1][i+1]==1 and array[r+2][i+2]==1 and array[r+3][i+3]==1:
                win=True
                print("Player 1 wins")
                break
            elif array[r][i]==2 and array[r+1][i+1]==2 and array[r+2][i+2]==2 and array[r+3][i+3]==2:
                win=True
                print("Player 2 wins")
                break
        if win == True:
                break
    return

def positiveDiagonalWin(array):
    win=False
    for i in range(columnsNo-3):
        for r in range(3,rowsNo):
            if array[r][i]==1 and array[r-1][i+1]==1 and array[r-2][i+2]==1 and array[r-3][i+3]==1:
                win=True
                print("Player 1 wins")
                break
            elif array[r][i]==2 and array[r-1][i+1]==2 and array[r-2][i+2]==2 and array[r-3][i+3]==2:
                win=True
                print("Player 2 wins")
                break
        if win == True:
                break
    return


def winningConditions(x):
    verticalWin(x)
    horizontalWin(x)
    negativeDiagonalWin(x)
    positiveDiagonalWin(x)

def validSpace(x):
    spaceFound=False
    for i in range(columnsNo):
        for r in range(rowsNo):
            if x[r][i]==0:
                spaceFound=True
                return spaceFound
    return spaceFound

playerNo=1
while(validSpace(board)):
    selectColumn(playerNo)
    playerNo+=1
    print(board)
    winningConditions(board)
