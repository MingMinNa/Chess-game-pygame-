import pygame
from typing import Sequence
from components.constants import *
from components.boardcell import *
from components.chesspiece import *


# process control
pygame.init()
pygame.display.set_caption("Chess Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
current_move = "White"


# chessboard spawn ("cells" is a List)
boardcell_sprite, cells = chessBoardGenerate()
chess_sprite, existing_chess = chessPiecesGenerate(cells)

choice = -1
move_area = []
# check whether you have moved the chessman(or alive): [Left Rook, King, Right Rook]
chess_castling = {"White": [True, True, True], "Black": [True, True, True]}
enemy_attack_area = []


# When you put the chessman down, this function will work
def renew_choice():
    global choice, move_area
    move_area.clear()
    choice = -1

# When you haven't chosen the chessman, this function will be called first.
# and it will return whether you pick the chessman
# True: you pick the chessman => variable "choice" is the chessman index in black(white)_chess and "move_area" will be updated
def choose_chesspiece() -> bool:
    global choice, move_area
    renew_choice()
    boardCellRecover(cells)
    
    for chess in existing_chess[current_move]:
        ret = chess.mouseTouch(mouse_pos, cells, chess_castling)
        if ret is None:
            chess.placeDown()
            return False
        else: 
            move_area = ret
            choice = existing_chess[current_move].index(chess)

# If you choose the next moval and the position is enemy, then remove the enemy from black(white)_chess and kill sprite
def killEnemy(current_move:str, move_area:Tuple[int], mouse_cell_pos:Tuple[int]) -> None:
    global existing_chess
    for i in range(len(existing_chess[current_move])):
        enemy_cell_x, enemy_cell_y = getCell((existing_chess[current_move][i].rect.x, existing_chess[current_move][i].rect.y))
        if (enemy_cell_x, enemy_cell_y) == mouse_cell_pos:
            cells[enemy_cell_x + enemy_cell_y * CELL_Col_Cnt].state = CELL_STATE["Nothing"]
            temp = existing_chess[current_move][i]
            if temp.chesskind == "Rook" and getCell((temp.rect.x, temp.rect.y) == (0, 0)):
                # left Rook is dead
                chess_castling[current_move][0] = False
            elif temp.chesskind == "Rook" and getCell((temp.rect.x, temp.rect.y) == (CELL_Col_Cnt - 1, 0)):
                # right Rook is dead
                chess_castling[current_move][2] = False
            elif temp.chesskind == "King":
                # King is dead, game end
                pass
                "GAME_END"
            existing_chess[current_move].pop(i)
            temp.kill()
            return
            
    raise Exception("enemy_idx Error")


while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            cell_x, cell_y = getCell(mouse_pos)

            # You have chosen the chessman and click the next moval position
            if len(move_area) != 0 and (cell_x, cell_y) in move_area:
                if cells[cell_x + cell_y * CELL_Col_Cnt].state != CELL_STATE["Nothing"]:
                    killEnemy(current_move, move_area, (cell_x, cell_y))

                
                existing_chess[current_move][choice].move(cell_x, cell_y, cells)
                renew_choice()
                if current_move == "White":
                    current_move = "Black"
                else:
                    renew_choice()
                    current_move = "White"

                flipBoard(cells, existing_chess)
            else:
                # when choice is not -1, then put the chessman down
                if choice != -1:
                    existing_chess[current_move][choice].placeDown()
                    choice = -1
                    boardCellRecover(cells)
                    continue
                choose_chesspiece()
                    
    screen.fill(BLACK)
    boardcell_sprite.draw(screen)
    chess_sprite.draw(screen)
    pygame.display.update()

pygame.quit()