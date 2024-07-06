import pygame
from typing import Sequence, Tuple
from components import *


class BoardCell(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, color:Sequence[int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((CELL_SIDE_LENGTH, CELL_SIDE_LENGTH))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.state = CELL_STATE["Nothing"]


# chessboard generator
def generate_chess_board() -> Tuple[Sequence["BoardCell"], "pygame.sprite.Group"]:
    boardcell_sprite = pygame.sprite.Group()

    # store all board cells in index 0 ~ 63
    cellList = []
    for i in range(CELL_ROW_CNT):
        # CELL_COLOR["Fisrt"] is green color, CELL_COLOR["Second"] is fresh_green color
        # color will change alternatingly
        '''
        First, Second, First, ...
        Second, First, Second, ...
        First, Second, First, ...
        Second, ...
        ...
        '''
        color_exchange = lambda x: CELL_COLOR["Second"] if x == CELL_COLOR["First"] else CELL_COLOR["First"]


        color = CELL_COLOR["First"]
        # vertical color change
        if i % 2 == 0:
            color = CELL_COLOR["Second"]

        for j in range(CELL_COL_CNT): 
            # horizontal color change 
            color = color_exchange(color)
            # store original color to another list for recoving the original color in the future
            CELL_COLOR_COPY.append(color)

            cell = BoardCell(x = (INIT_x + CELL_SIDE_LENGTH * j), y = (INIT_y + CELL_SIDE_LENGTH * i),color = color)
            cellList.append(cell)
            boardcell_sprite.add(cell)
    return boardcell_sprite, cellList

# recover the cell color to green and fresh_green
def recover_boardCell(cells: Sequence["BoardCell"]) -> None:
    for i in range(CELL_COL_CNT * CELL_ROW_CNT):
        cells[i].image.fill(CELL_COLOR_COPY[i])


# transform the (pixel_x, pixel_y) to (cell_x, cell_y)
def get_cell(pos:Sequence[int]) -> Tuple[int]:
    return ((pos[0] - INIT_x) // CELL_SIDE_LENGTH, (pos[1] - INIT_y) // CELL_SIDE_LENGTH)


