
def evaluate (board):
    #show the status of the game, _ = game not finished, ! = draw, x = player with xs has won, o = player with os has won
    if 'xxx' in board:
        return 'x'
    elif 'ooo' in board:
        return 'o'
    elif '-' not in board:
        return '!'
    else:
        return'-'
    

def move (board, position_number, mark):
    # returns the game board with given mark on given position
    position_number_trans = position_number -1 
    # because python starts to count at 0 and then it would always be the chosen position + 1

    board = board[:position_number_trans] + mark + board[position_number_trans + 1:20]
    return board 


def player_move (board):
    # to get the input of the player
    while True:
        player_inp = int(input('Please enter a number between 1 and 20: '))
        if player_inp <1:
            print('Please enter a number in the given range!')
        elif player_inp >20:
            print('Please enter a number in the given range!')
        elif board[player_inp-1] == 'x':
            print('This spot is already taken by you, please chose another one!')
        elif board[player_inp-1] == 'o':
            print('This spot is already taken by the computer, please chose another one!')
        else:
            board = move(board, player_inp, 'x')
            return board


def pc_move(board):
# to get the pc's move on the board
    from random import randrange
    while True:
        computer_inp = (randrange(0,19))
        if board[computer_inp] in ('x', 'o'):
            computer_inp = (randrange(0,19))
        elif board[computer_inp] == '-':
            board = move(board, computer_inp, 'o')
            break
    return board

#I tried a LOT of different ways here to prevent the computer to overwrite marks that
#are already on the board, however I was not successful. I also tried without a while loop,
#so only if conditions, and also some stuff which probably does not make sense (I was already
# a litte desperate haha). I hope it is fine that I still sumbitted what i managed to do and I 
# hope that someone can give me feedback here on what I did wrong. If you need me to re-submit 
# afterwards for the project to count as submitted, please let me know :)


def oneD_tictactoe():

    board = '--------------------'

    while '-' in board:
        board = (player_move(board))
        board = (pc_move(board))
        print(board)
        print(evaluate(board))
        if evaluate(board) == 'x':
            print('You won!')
            break
        elif evaluate(board) == 'o':
            print('You lost!')
            break
        elif evaluate(board) == '!':
            print('Draw! Start a new game!')
            break
    return board

print(oneD_tictactoe())