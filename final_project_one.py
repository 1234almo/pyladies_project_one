
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