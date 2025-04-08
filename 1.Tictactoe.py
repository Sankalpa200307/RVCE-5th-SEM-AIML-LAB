def printboard(board):
    for row in board:
        print(" | ".join(row))
        print("-"*10)

def isfull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                return False

    return True

def iswinner(board, player):
    return (any(all(board[i][j]==player for j in range(3)) for i in range(3)) or
            any(all(board[j][i]==player for j in range(3)) for i in range(3)) or 
            all(board[i][i]==player for i in range(3)) or 
            all(board[i][2-i]==player for i in range(3)))


def minimax(board, maximizing):
    if iswinner(board, 'X'):
        return -1
    if iswinner(board, 'O'):
        return 1   
    if isfull(board):
        return 0  

    if maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, False))
                    board[i][j] = ' '
        return best

    else:
          best = float('inf')
          for i in range(3):
              for j in range(3):
                  if board[i][j] == ' ':
                      board[i][j] = 'X'  
                      best = min(best, minimax(board, True))
                      board[i][j] = ' '
          return best

def getbestmove(board):
    bestmove, bestscore = None, -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '                                          
                if score>bestscore:
                    bestmove, bestscore = (i, j), score
    return bestmove               



def playgame():
    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

    while not iswinner(board, 'X') and not iswinner(board, 'O') and not isfull(board):
        printboard(board)
        row = int(input("Enter the row "))
        col = int(input("Enter the col "))
        board[row][col] = 'X'

        if not isfull(board) and not iswinner(board, 'X'):
            move = getbestmove(board)
            if move:
                board[move[0]][move[1]] = 'O'

    printboard(board)
    if iswinner(board, 'X'):
        print("you win")
    elif iswinner(board, 'O'):
        print("AI win")
    else:
        print("Draw")

playgame()