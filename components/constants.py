import os
import pygame



# windows constants
WIDTH, HEIGHT = 700, 700 
FPS = 60

# color 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
GREEN = (0, 110, 0)
Freash_Green = (99,211,108)
RED = (255, 0, 0)

# board cell 
CELL_SideLength = 80
CELL_Col_Cnt, CELL_Row_Cnt = 8, 8
INIT_x, INIT_y = 30, 30 # Cell init
CELL_COLOR = {"First": GREEN, "Second": Freash_Green}
CELL_STATE = {"Nothing":2 , "White":0, "Black": 1} 
CELL_COLOR_COPY = []

# chessPieces
# CHESSMAP = {
#     "King":  0,
#     "Queen": 1,
#     "Rook":  2,
#     "Bishop":3,
#     "Knight":4,
#     "Pawn":  5
# }

CHESS_SideLength = 60
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

CHESSMOVE = {
    "King":   [[[-1,-1]], [[-1, 0]], [[-1, 1]], [[0, -1]], [[0, 1]], [[1, -1]], [[1, 0]], [[1, 1]]],
    "Queen":  [Up, Down, Left, Right, UpLeft, UpRight, DownLeft, DownRight],
    "Rook":   [Up, Down, Left, Right],
    "Bishop": [UpLeft, UpRight, DownLeft, DownRight],
    "Knight": [[[-1, -2]], [[-2, -1]], [[1, -2]], [[2, -1]], [[1, 2]], [[2, 1]], [[-2, 1]], [[-1, 2]]]
} # Pawn will be as a exception case

CHESS_COLOR = {
    "Enemy": RED,
    "Space": GRAY
}
