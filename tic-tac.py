import random
########################
## Setting up the board
#
def draw_board(board):
    print(' | |')
    print('' + board[1] + '|' + board[2] + '|' + board[3])
    print(' | |')
    print('' + board[4] + '|' + board[5] + '|' + board[6])
    print(' | |')
    print('' + board[7] + '|' + board[8] + '|' + board[9])
    print(' | |')

def player_input():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        input('Player 1: Do you want to be X or O?')
        letter = input.upper()
    if letter == 'X':
        return('X', 'O')
    return('O', 'X')

def choose_first():
    if random.randint(1,2) == 1:
        return 'Player1'
    return 'Player2'

#######################
## Player1's decisions
#
def player_choice():
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose the next free space: (1-9)')
    return int(position)

def make_move(board, letter, position):
    board[position] = letter

def play_again():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

##################################
## Player2's (computer) decisions
#
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if space_check(board, position):
            possibleMoves.append(i)
        elif len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

##############################
## Checking board real estate
#
def space_check(board, position):
    return board[position] = ''

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def full_board_check(board):
    for i in range(1,10):
        return space_check(board, i)

#################
## Algorithm
#
print('Welcome to Tic Tac Toe!')

while True:
    #Reset the board
    theBoard = [''] * 10
    playerLetter, computerLetter = player_input()
    startingPlayer = choose_first()
    print(startingPlayer + ' will go first!')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player1':
        #player's turn
        draw_board(theBoard)
        make_move(theBoard, playerLetter, move)

        if win_check(board, mark):
            draw_board(theBoard)
            print(turn + 'has won the game!')
            gameIsPlaying = False
        else:
            if full_board_check(theBoard):
            draw_board(theBoard)
            print('The game is a tie!')
            break
        else:
            turn = 'Player2'

    if not play_again():
        break
