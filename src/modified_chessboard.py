import sys, copy

STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = '  '


def print_chess_board(board):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':
            #print(x, y, is_white_square)  # DEBUG: Shows coordinates in order.
            if x + y in board.keys():
              squares.append(board[x + y])
            else:
              if is_white_square:
                squares.append(WHITE_SQUARE)
              else:
                squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))

def print_help():
    print('Interactive Chess Board')
    print('by Al Sweigart al@inventwithpython.com')
    print()
    print('Pieces:')
    print('  w - White, b - Black')
    print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
    print('Commands:')
    print('  move e2 e4 - Moves the piece at e2 to e4.')
    print('  remove e2 - Removes the piece at e2.')
    print('  set e2 wP - Sets square e2 to a white pawn.')
    print('  reset - Reset pieces back to their starting squares.')
    print('  clear - Clear the entire board.')
    print('  fill wP - Fill entire board with white pawns.')
    print('  help - Show this help information.')
    print('  quit - Quits the program.')

def isBoardValid(dict):
    valid = True
    
    black_king=0
    black_pawns=0
    black_pieces=0
    white_king=0
    white_pawns=0
    white_pieces=0
    
    for k, v  in dict.items():
        if v.startswith('b') and v== "bK":
            black_pieces +=1
            black_king +=1
        elif v.startswith('b') and v== "bP":
            black_pieces +=1
            black_pawns +=1
        elif v.startswith('b'):
            black_pieces +=1
        elif v.startswith('w') and v== "wK":
            white_pieces +=1
            white_king +=1
        elif v.startswith('w') and v== "wP":
            white_pieces +=1
            white_pawns +=1
        elif v.startswith('w'):
            white_pieces +=1
        if not (k.startswith (("a","b","c","d","e","f","g","h")) and k.endswith(("1","2","3","4","5","6","7","8"))):
            valid = False
        if not (v.startswith(("w","b")) and v.endswith(("P","K","Q","N","R","B"))):
            valid = False
    if black_king !=1 or white_king !=1 or black_pieces>16 or black_pawns>8 or white_pieces>16 or white_pawns>8:
        valid = False
        print(f"Pieces not correct! \nYou have {black_king} black king and {white_king} white king\nThe black pawns are {black_pawns} and the white pawns are{white_pawns}\nThe number of black pieces are {black_pieces} and the number of white pieces are {white_pieces}")
 



    return valid

print(isBoardValid(STARTING_PIECES))

main_board = copy.copy(STARTING_PIECES)
print_help()
while True:
    print_chess_board(main_board)
    response = input('> ').split()

    if response[0] == 'move':
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]
    elif response[0] == 'remove':
        del main_board[response[1]]
    elif response[0] == 'set':
        main_board[response[1]] = response[2]
    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == 'clear':
        main_board = {}
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]
    elif response[0] == 'help':
        print_help()
    elif response[0] == 'quit':
        sys.exit()
    print(isBoardValid(main_board))