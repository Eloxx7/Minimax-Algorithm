class GameState:
    def __init__(self, board, current_player):
        # board is a list of lists, e.g. board[row][col]
        self.board = board
        self.current_player = current_player  # 'B' or 'W'
        self.rows = len(board)
        self.cols = len(board[0])

    def copy(self):
        return GameState(
            [row[:] for row in self.board],
            self.current_player
        )
    
def make_default_board(rows=8, cols=8):
    board = [['_'] * cols for _ in range(rows)]
    # B occupies the top two rows (rows 0 and 1)
    for r in range(2):
        for c in range(cols):
            board[r][c] = 'B'
    # W occupies the bottom two rows
    for r in range(rows - 2, rows):
        for c in range(cols):
            board[r][c] = 'W'
    return board

def print_board(state):
    rows = state.rows
    cols = state.cols
    
    # Column headers (a, b, c, ...)
    col_labels = '  ' + ' '.join(chr(ord('a') + c) for c in range(cols))
    print(col_labels)
    
    for r in range(rows):
        # Row number (counting from bottom like chess, so row 0 = highest number)
        row_label = rows - r
        row_str = ' '.join(state.board[r][c] for c in range(cols))
        print(f"{row_label} {row_str} {row_label}")
    
    print(col_labels)
    print(f"Current player: {state.current_player}")

def move_generator(state):
    # Placeholder for move generation logic
    # This should return a list of valid moves for the current player
    rows = state.rows
    cols = state.cols
    moves = []
    direction = 1 if state.current_player == 'B' else -1  # B moves down, W moves up
    for r in range(rows):
        for c in range(cols):
            if state.board[r][c] == state.current_player:
                # Check possible moves for this piece
                current_moves = []
                opponent = 'W' if state.current_player == 'B' else 'B'
                    # B moves downwards
                if r + direction < rows and state.board[r + direction][c] == '_':
                        current_moves.append((r, c, r + direction, c))  
                if r + direction < rows and c - 1 >= 0 and (state.board[r + direction][c - 1] == '_' or state.board[r + direction][c - 1] == opponent):
                        current_moves.append((r, c, r + direction, c - 1))
                if r + direction < rows and c + 1 < cols and (state.board[r + direction][c + 1] == '_' or state.board[r + direction][c + 1] == opponent):
                        current_moves.append((r, c, r + direction, c + 1))
                    # W moves upwards
                pass
                moves.extend(current_moves)
    return moves

state = GameState(make_default_board(), 'B')
moves = move_generator(state)
print("Possible moves for player B:")
for move in moves:
    print(move)
print_board(state)