import numpy as np
rowsNo=6
columnsNo=7
WINDOW_LENGTH = 4

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
    
def evaluate_window(window, piece):
    score = 0
    opp_piece = 1
    if piece == 1:
        opp_piece = 2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(board[:, columnsNo//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(rowsNo):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(columnsNo-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score Vertical
    for c in range(columnsNo):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(rowsNo-3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score posiive sloped diagonal
    for r in range(rowsNo-3):
        for c in range(columnsNo-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(rowsNo-3):
        for c in range(columnsNo-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score        
    

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
