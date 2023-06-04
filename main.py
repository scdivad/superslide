import random

R = 5
C = 4
board = [[None for x in range(C)] for y in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def print_board(board):
    for row in board:
        print(row)

# returns a random integer between a and b, inclusive
def rng(a, b):
    return random.randint(a, b)

def in_bounds(x, y):
    return x >= 0 and x < R and y >= 0 and y < C

def try_n_times(n, func): # extremely lazy way to do this, its like janky backtracking but the board is only 5x4
    for _ in range(n):
        if func(): 
            return True
    return False

def place_red_piece():
    while True:
        x = rng(0, R-2)
        y = rng(0, C-2)
        if not (x == 3 and y == 1):
            board[x][y] = board[x+1][y] = board[x][y+1] = board[x+1][y+1] = 'R'
            break

def place_blue_yellow_pieces(num_blues, num_yellows):
    def place_blue_piece():
        x = rng(0, R-1)
        y = rng(0, C-1)
        direction = rng(0, 3)
        x2 = x + dx[direction]
        y2 = y + dy[direction]
        if in_bounds(x2, y2) and not board[x][y] and not board[x2][y2]:
            board[x][y] = 'B'
            board[x2][y2] = 'B'
            return True
        return False
    
    for j in range(num_blues):
        res = try_n_times(100, place_blue_piece)
        if not res:
            return False

    for i in range(num_yellows):
        x = rng(0, R-1)
        y = rng(0, C-1)
        if not board[x][y]:
            board[x][y] = 'Y'

    return True

while True:
    place_red_piece()

    num_blues = rng(0, 5)       # 2x1 pieces
    num_yellows = rng(0, 12)    # 1x1 pieces

    # Randomly place the blue and yellow pieces on the board
    res = try_n_times(100, lambda: place_blue_yellow_pieces(num_blues, num_yellows))
    if res:
        break

# board created
print_board(board)

# start game

# https://www.youtube.com/watch?v=uGmMsGOcBB0