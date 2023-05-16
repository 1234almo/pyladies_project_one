
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