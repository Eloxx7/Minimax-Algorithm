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