
# windows constants
INIT_WIDTH, INIT_HEIGHT = 700, 550
WIDTH, HEIGHT = 700, 700 
FPS = 60

# color 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (125, 125, 125)
GREEN = (0, 110, 0)
FRESH_GREEN = (99,211,108)
RED = (255, 0, 0)
YELLOW = (240, 230, 140)
BLUE = (30, 144, 255)

# board cell 
CELL_SIDE_LENGTH = 80
CELL_COL_CNT, CELL_ROW_CNT = 8, 8
INIT_x, INIT_y = 30, 30 # Cell init
CELL_COLOR = {"First": GREEN, "Second": FRESH_GREEN}
CELL_STATE = {"Nothing":2 , "White":0, "Black": 1} 
CELL_COLOR_COPY = []
CELL_COLOR_BASE_ON_CHESS = {
    "Enemy": RED,
    "Space": GRAY,
    "Castling":YELLOW,
    "Promotion":BLUE
}
# chessPieces

CHESS_SIDE_LENGTH = 60
CHESS_STATE = {"Up":0 , "Down": 1}
TEAM = {"White":0 , "Black": 1}
# [x, y]
Up = [[0, -i] for i in range(1, 9, 1)]
Down = [[0, i] for i in range(1, 9)]
Left = [[-i, 0] for i in range(1, 9)]
Right = [[i, 0] for i in range(1, 9)]
UpLeft = [[-i, -i] for i in range(1, 9)]
UpRight = [[i, -i] for i in range(1, 9)]
DownLeft = [[-i, i] for i in range(1, 9)]
DownRight = [[i, i] for i in range(1, 9)]

CHESS_MOVE = {
    "King":   [[[-1,-1]], [[-1, 0]], [[-1, 1]], [[0, -1]], [[0, 1]], [[1, -1]], [[1, 0]], [[1, 1]]],
    "Queen":  [Up, Down, Left, Right, UpLeft, UpRight, DownLeft, DownRight],
    "Rook":   [Up, Down, Left, Right],
    "Bishop": [UpLeft, UpRight, DownLeft, DownRight],
    "Knight": [[[-1, -2]], [[-2, -1]], [[1, -2]], [[2, -1]], [[1, 2]], [[2, 1]], [[-2, 1]], [[-1, 2]]]
} # Pawn will be as a exception case
Pawn_EnPassant = {
    "None": -1,
    "Loss Chance": -2
}

CASTLING_MOVE = {
    "Short":{
        "Original_King":(3, CELL_ROW_CNT - 1),
        "Original_Rook":(0, CELL_ROW_CNT - 1),
        "King":(1, CELL_ROW_CNT - 1),
        "Rook":(2, CELL_ROW_CNT - 1)
    },
    "Long":{
        "Original_King":(3, CELL_ROW_CNT - 1),
        "Original_Rook":(CELL_COL_CNT - 1, CELL_ROW_CNT - 1),
        "King":(5, CELL_ROW_CNT - 1),
        "Rook":(4, CELL_ROW_CNT - 1)
    }
}

# promotion panel
PANEL_WIDTH = 400
PANEL_HEIGHT = 250
PANEL_INIT_X = 150
PANEL_INIT_Y = 225
