import numpy as np
import math
rowsNo=6
WINDOW_LENGTH = 4
columnsNo=7
winFlag = False
player1win = False
player2win = False

board=np.zeros((rowsNo,columnsNo))
print (board)

def selectColumn(player):
    pieceLocation = input("In which column you want to place your piece?")
    i=1
    if validColumn(board,int(pieceLocation)-1):
        while(board[rowsNo-i][int(pieceLocation)-1]!=0):
            i+=1
        if player%2!=0 :
            board[rowsNo - i][int(pieceLocation) - 1] = 1
        elif player%2==0 :
            board[rowsNo - i][int(pieceLocation) - 1] = 2
        return pieceLocation
    else:
        print("Column Full")
        selectColumn(player)
        

def dropPiece(board,pieceLocation,piece):
    i=1
    while(board[rowsNo-i][int(pieceLocation)]!=0):
        i+=1
    board[rowsNo - i][int(pieceLocation)] = piece
        
def validColumn(x,columnNumber):
    for r in range(rowsNo):
        if x[r][columnNumber]==0:
            return True
        
    return False

def horizontalWin(array):
    global winFlag
    global player1win
    global player2win
    global horizontal_flag_1
    global horizontal_flag_2
    horizontal_flag_1=0
    horizontal_flag_2=0
    transposed=array.T
    for i in range(rowsNo):
        for r in range(columnsNo):
            if transposed[r][i]==1:
                horizontal_flag_1+=1
                if horizontal_flag_1==4:
                    print("Player 1 wins")
                    player1win=True
                    winFlag=True
                    break
            else:
                horizontal_flag_1=0
            if transposed[r][i]==2:
                horizontal_flag_2+=1
                if horizontal_flag_2==4:
                    print("AI wins")
                    winFlag = True
                    player2win=True
                    break
            else:
                horizontal_flag_2=0
        horizontal_flag_1 = 0
        horizontal_flag_2 = 0
        if horizontal_flag_1==4:
        	horizontal_flag_1=0
        	break
        elif horizontal_flag_2==4:
            horizontal_flag_2=0
            break
    return

def verticalWin(array):
    global winFlag
    global player1win
    global player2win
    global vertical_flag_1
    global vertical_flag_2
    vertical_flag_1=0
    vertical_flag_2=0
    for i in range(columnsNo):
        for r in range(rowsNo):
            if array[r][i]==1:
                vertical_flag_1+=1
                if vertical_flag_1==4:
                    print("Player 1 wins")
                    winFlag = True
                    player1win=True
                    break
            else:
                vertical_flag_1=0
            if array[r][i]==2:
                vertical_flag_2+=1
                if vertical_flag_2==4:
                    print("AI wins")
                    winFlag = True
                    player2win=True
                    break
            else:
                vertical_flag_2=0
        if vertical_flag_1==4:
        	vertical_flag_1=0
        	break
        elif vertical_flag_2==4:
            vertical_flag_2=0
            break
    vertical_flag_1=0
    vertical_flag_2=0
    return

def negativeDiagonalWin(array):
    global winFlag
    global player1win
    global player2win
    win=False
    for i in range(columnsNo-3):
        for r in range(rowsNo-3):
            if array[r][i]==1 and array[r+1][i+1]==1 and array[r+2][i+2]==1 and array[r+3][i+3]==1:
                win=True
                print("Player 1 wins")
                winFlag = True
                player1win=True
                break
            elif array[r][i]==2 and array[r+1][i+1]==2 and array[r+2][i+2]==2 and array[r+3][i+3]==2:
                win=True
                print("AI wins")
                winFlag = True
                player2win=True
                break
        if win == True:
                break
    return

def positiveDiagonalWin(array):
    global winFlag
    global player1win
    global player2win
    win=False
    for i in range(columnsNo-3):
        for r in range(3,rowsNo):
            if array[r][i]==1 and array[r-1][i+1]==1 and array[r-2][i+2]==1 and array[r-3][i+3]==1:
                win=True
                print("Player 1 wins")
                winFlag = True
                player1win=True
                break
            elif array[r][i]==2 and array[r-1][i+1]==2 and array[r-2][i+2]==2 and array[r-3][i+3]==2:
                win=True
                print("AI wins")
                winFlag = True
                player2win=True
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
        score -= 3 * difficulty

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

def newValidLocations(board):
    listNewValidLocations=[]
    for i in range(columnsNo):
        if(validColumn(board,i) == True ):
    #       print(boardI)
            listNewValidLocations.append(i)
            
   #print (listNewValidLocations)
    return listNewValidLocations

def minimax(board,depth,alpha,beta,MaxPlayer):
    newLocations=newValidLocations(board)
    #print (newLocations)
    if depth ==0 or winFlag:
        if depth == 0:
            return (None , score_position(board,2))
        else :
            if player1win:
                return(None, -100000 )
            elif player2win:
                return(None, 100000)
            else: #no win
                return(None,0)
    if MaxPlayer:
        value=-math.inf
        colToPlay=0
        for i in newLocations:
            newBoard=board.copy()
            dropPiece(newBoard,i,2)
            _,score = minimax(newBoard,depth-1,alpha,beta,False)
            if score>value:
                colToPlay=i
                value=score
            alpha=max(alpha,value)
            if beta < alpha :
                break
        return colToPlay,value
    
    else:
        value=math.inf
        colToPlay=0
        for i in newLocations:
            newBoard=board.copy()
            dropPiece(newBoard,i,1)
            _,score = minimax(newBoard,depth-1,alpha,beta,True)
            if score<value:
                colToPlay=i
                value=score
            beta=min(beta,value)
            if beta < alpha :
                break
        return colToPlay,value

startPlayer = int(input("Type 1 for player to start or any other number for AI to start the game!"))
difficulty = int(input("Pick difficulty level from 1 to 8 (Picking anything above 4 might take some time for AI to play)"))
if startPlayer == 1:
    while(validSpace(board)):
        selectColumn(1)
        winningConditions(board)
        if winFlag==True:
            print(board)
            input("Press any key to exit")
            break
        col, score = minimax(board,difficulty,-math.inf,math.inf,True)
        dropPiece(board,col,2)
        print(col+1,"AI score: ",score)
        print(board)
        winningConditions(board)
        if winFlag==True:
            input("Press any key to exit")
            break
else:
    while(validSpace(board)):
        col, score = minimax(board,difficulty,-math.inf,math.inf,True)
        dropPiece(board,col,2)
        winningConditions(board)
        print(col+1,"AI score: ",score)
        print(board)
        if winFlag==True:
            input("Press any key to exit")
            break
        selectColumn(1)
        winningConditions(board)
        if winFlag==True:
            print(board)
            input("Press any key to exit")
            break
