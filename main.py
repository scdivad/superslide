import random

R = 5
C = 4

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

def place_pieces(num_blues, num_yellows):
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
        blue_placed = False
        for _ in range(100):
            blue_placed = place_blue_piece()
            if blue_placed:
                break
        if not blue_placed:
            return False

    for i in range(num_yellows):
        x = rng(0, R-1)
        y = rng(0, C-1)
        if not board[x][y]:
            board[x][y] = 'Y'

    return True

board = [[None for x in range(C)] for y in range(R)]

pieces_placed = False
while not pieces_placed:
    num_blues = rng(0, 5)       # 2x1 pieces
    num_yellows = rng(0, 12)    # 1x1 pieces

    # Choose random spot for the red piece (2x2)
    while True:
        x = rng(0, R-2)
        y = rng(0, C-2)
        if not (x == 3 and y == 1):
            board[x][y] = board[x+1][y] = board[x][y+1] = board[x+1][y+1] = 'R'
            break

    # Randomly place the blue and yellow pieces on the board
    for t in range(100):
        pieces_placed = place_pieces(num_blues, num_yellows)
        if pieces_placed:
            break
    
    if pieces_placed:
        break

print_board(board)

# https://www.youtube.com/watch?v=uGmMsGOcBB0