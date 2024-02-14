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
def choose_chesspiece() -> None:
    global choice, move_area, mouse_pos, enemy_attack_area, existing_chess
    renew_choice()
    boardCellRecover(cells)
    
    for chess in existing_chess[current_move]:
        ret = chess.mouseTouch(mouse_pos, cells, chess_castling, enemy_attack_area, existing_chess)
        if ret is None:
            chess.placeDown()
        else: 
            move_area = ret
            choice = existing_chess[current_move].index(chess)

# If you choose the next moval and the position is enemy, then remove the enemy from black(white)_chess and kill sprite
def killEnemy(current_move:str, move_area:Tuple[int], mouse_cell_pos:Tuple[int]) -> None:
    global existing_chess
    if current_move == "White":
        enemy_color = "Black"
    else:
        enemy_color = "White"
    for i in range(len(existing_chess[enemy_color])):
        enemy_cell_x, enemy_cell_y = getCell((existing_chess[enemy_color][i].rect.x, existing_chess[enemy_color][i].rect.y))
        if (enemy_cell_x, enemy_cell_y) == mouse_cell_pos:
            cells[enemy_cell_x + enemy_cell_y * CELL_Col_Cnt].state = CELL_STATE["Nothing"]
            temp = existing_chess[enemy_color][i]
            if temp.chesskind == "Rook" and getCell((temp.rect.x, temp.rect.y)) == (0, 0):
                # left Rook is dead
                chess_castling[enemy_color][0] = False
            elif temp.chesskind == "Rook" and getCell((temp.rect.x, temp.rect.y)) == (CELL_Col_Cnt - 1, 0):
                # right Rook is dead
                chess_castling[enemy_color][2] = False
            elif temp.chesskind == "King":
                # King is dead, game end
                pass
                "GAME_END"
            existing_chess[enemy_color].pop(i)
            temp.kill()
            return
            
    raise Exception("enemy_idx Error")

def calculate_EnemyAttackArea(enemy_attack_area:list[Tuple[int]], existing_chess:Mapping[str, list["Chesspiece"]], current_move:str, cells: Sequence["BoardCell"]) -> None:
    enemy_attack_area.clear()
    if current_move == "White":
        enemy_color = "Black"
    else:
        enemy_color = "White"

    # Add Pawn path
    ChessMove = CHESSMOVE.copy()
    ChessMove["Pawn"] = [[[-1, 1]], [[1, 1]]]


    for chessman in existing_chess[enemy_color]:
        chessman_x, chessman_y = getCell((chessman.rect.x, chessman.rect.y))
        for dir in ChessMove[chessman.chesskind]:
            for subdir in dir:
                pos_x, pos_y = chessman_x + subdir[0], chessman_y + subdir[1]
                if pos_x < 0 or pos_x >= 8 or pos_y < 0 or pos_y >= 8:
                    continue
                enemy_attack_area.append((pos_x, pos_y))
                if cells[pos_x + pos_y * CELL_Col_Cnt].state != CELL_STATE["Nothing"]:
                    break
    
    del ChessMove

def checkCastlingClick( existing_chess: Mapping[str, Sequence["Chesspiece"]], cells:Sequence["BoardCell"], mouse_cell_pos:Tuple[int]) -> None:
    if mouse_cell_pos not in CastlingMOVE["Short"]["King"] and \
       mouse_cell_pos  not in CastlingMOVE["Long"]["King"]:
        return


    for dist in ("Short", "Long"):
        king_cell_x , king_cell_y = getCell((existing_chess[current_move][choice].rect.x, existing_chess[current_move][choice].rect.y))
        if (king_cell_x, king_cell_y) == CastlingMOVE[dist]["Original_King"]:
            # find RootIdx
            RookIdx = None
            for i in range(len(existing_chess[current_move])):
                rook_cell_x, rook_cell_y = getCell((existing_chess[current_move][i].rect.x, existing_chess[current_move][i].rect.y))
                if (rook_cell_x, rook_cell_y) == CastlingMOVE[dist]["Original_Rook"]:
                    RootIdx = i
                    break
                # fail to find Idx
            if RookIdx is None:
                continue
            existing_chess[current_move][RootIdx].move(cell_x = CastlingMOVE[dist]["Rook"][0], cell_y = CastlingMOVE[dist]["Rook"][1], cells = cells)


while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            calculate_EnemyAttackArea(enemy_attack_area, existing_chess, current_move, cells)
            mouse_pos = pygame.mouse.get_pos()
            cell_x, cell_y = getCell(mouse_pos)
            # You have chosen the chessman and click the next moval position
            if choice != -1 and len(move_area) != 0 and (cell_x, cell_y) in move_area:
               
                
                if existing_chess[current_move][choice].chesskind == "Pawn":
                    pawn_cell_x, pawn_cell_y = getCell((existing_chess[current_move][choice].rect.x, existing_chess[current_move][choice].rect.y))
                    # The first case is en passant
                        # en_passant >= 0 => Not "None" and "Loss chance"
                    if  existing_chess[current_move][choice].en_passant >= 0 and \
                        abs(cell_x - pawn_cell_x) == 1 and \
                        cells[cell_x  + CELL_Col_Cnt * cell_y].state == CELL_STATE["Nothing"]:
                        killEnemy(current_move, move_area, (cell_x, cell_y + 1))
                    # The second case: first step (move 2 cell) => then we set the left(right) enemy pawn en_passant (if any)
                    elif abs(pawn_cell_y - cell_y) == 2:
                        enemy_color = "White" if current_move == "Black" else "Black"
                        for chess in existing_chess[enemy_color]:
                            enemy_x, enemy_y = getCell((chess.rect.x, chess.rect.y))
                            if chess.chesskind == "Pawn" and abs(enemy_x - cell_x) == 1 and enemy_y == cell_y:
                                chess.en_passant = choice

                 # If the cell you click has enemy, kill it
                if cells[cell_x + cell_y * CELL_Col_Cnt].state != CELL_STATE["Nothing"]:
                    killEnemy(current_move, move_area, (cell_x, cell_y))

                # Castling handling
                if existing_chess[current_move][choice].chesskind == "King":
                    checkCastlingClick(existing_chess, cells, (cell_x, cell_y))
                    chess_castling[current_move][1] = False
                elif existing_chess[current_move][choice].chesskind == "Rook":
                    current_cell_x , current_cell_y = getCell((existing_chess[current_move][choice].rect.x, existing_chess[current_move][choice].rect.y))
                    if (current_cell_x, current_cell_y) == (0, CELL_Row_Cnt - 1):
                        chess_castling[current_move][0] = False
                    elif (current_cell_x, current_cell_y) == (CELL_Col_Cnt - 1, CELL_Row_Cnt - 1):
                        chess_castling[current_move][2] = False

                for chess in existing_chess[current_move]:
                    if chess.chesskind == "Pawn":
                        if chess.en_passant >= 0:
                            chess.en_passant = Pawn_EnPassant["Loss Chance"]

                existing_chess[current_move][choice].move(cell_x, cell_y, cells)
                if existing_chess[current_move][choice].chesskind == "Pawn" and cell_y == 0:
                    pawn_Promotion(existing_chess[current_move][choice])


                renew_choice()
                if current_move == "White":
                    current_move = "Black"
                else:
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