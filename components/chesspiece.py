import pygame 
from typing import Sequence, Tuple, Optional, Mapping
from components import *
from components.boardcell import *

class Chesspiece(pygame.sprite.Sprite):
    def __init__(self, chesskind:str, cell_x:int, cell_y:int, team:str, cells:list["BoardCell"], chessman_img:Mapping[str, Mapping[str,"pygame.Surface"]]) -> None:
        
        # new chesspiece must be spawned in the empty cell
        if cells[cell_x  + cell_y * CELL_COL_CNT].state != CELL_STATE["Nothing"]:
            raise Exception("The position have other chess")

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(chessman_img[team][chesskind], (CHESS_SIDE_LENGTH, CHESS_SIDE_LENGTH))
        self.image.set_colorkey(RED)
        # which color does the chessman belong to 
        self.team = TEAM[team]

        # set the position
        self.rect = self.image.get_rect()
        self.rect.x = INIT_x + cell_x * CELL_SIDE_LENGTH + 10
        self.rect.y = INIT_y + cell_y * CELL_SIDE_LENGTH + 10
        
        # chesskind: [King, Queen, Knight, Rook, Bishop, Pawn]
        self.chesskind = chesskind
        if self.chesskind == "Pawn":
            # Pawn unique attribute
            # This will store enemy Pawn index that you can eat it by en_passant
            self.en_passant = Pawn_EnPassant["None"] 

        # if state is Up => show the cells which this chessman can move
        # (Like you take the chessman up, and this will show which position you can put it on)
        self.state = CHESS_STATE["Down"]

        # update the cells state, TEAM encoding way is same as CELL_STATE although this will confuse someone.
        #       TEAM = {"White":0 , "Black": 1}
        # CELL_STATE = {"White":0 , "Black": 1, "Nothing":2} 
        cells[cell_x  + cell_y * CELL_COL_CNT].state = TEAM[team]

    # when you click the mouse button, test whether this chessman is pointed by mouse cursor
    def mouse_click(self, mouse_pos: Tuple[int], cells:Sequence["BoardCell"],castling:Mapping[str, list[bool]], enemy_attack: list[Tuple[int]], existing_chess:Mapping[str, Sequence["Chesspiece"]]) -> Optional[list[Tuple[int]]]:
        x, y = mouse_pos
        if (self.rect.x > x or x > self.rect.x + CHESS_SIDE_LENGTH) or \
           (self.rect.y > y or y > self.rect.y + CHESS_SIDE_LENGTH):
            return None

        # after you click the chessman
        # if the chessman is Down, pick it up and find the movable positions(then show).
        # if the chessman is Up, put it down and cancel the moval hint.
        if self.state == CHESS_STATE["Down"]:
            self.place_up()
            # find the movable positions
            return self.show_movable(cells, castling, enemy_attack, existing_chess)
        else:
            self.place_down()
            # cancel the moval hint
            recover_boardCell(cells)
            return None
    
    # put the chessman down
    def place_down(self) -> None:
        if self.state == CHESS_STATE["Up"]:
            self.state = CHESS_STATE["Down"]
            self.rect.y += 10

    # pick the chessman up
    def place_up(self) -> None:
        if self.state == CHESS_STATE["Down"]:
            self.state = CHESS_STATE["Up"]
            self.rect.y -= 10
 
    def show_movable(self, cells:Sequence["BoardCell"], castling:Mapping[str, list[bool]], enemy_attack: list[Tuple[int]], existing_chess:Mapping[str, Sequence["Chesspiece"]]) -> list[Tuple[int]]:
        # First, recover the cell color to avoid other chessman hint affecting our result
        recover_boardCell(cells)

        enemy_color = "White" if self.team == TEAM["Black"] else "Black"
        teamColor = "White" if self.team  == TEAM["White"]  else "Black"

        cell_x, cell_y = get_cell((self.rect.x, self.rect.y))

        movableList = []
        # since Pawn have more complicated rule such as "promotion" and "en passant", I will see it as an exception case
        if self.chesskind == "Pawn":

            cell_x, cell_y = get_cell((self.rect.x, self.rect.y))
            # First Step: Go Forward 
            if cell_y == CELL_COL_CNT - 2:
                for i in range(1, 3):
                    if cells[CELL_COL_CNT * (cell_y - i) + cell_x].state == CELL_STATE["Nothing"]:
                        cells[CELL_COL_CNT * (cell_y - i) + cell_x].image.fill(CELL_COLOR_BASE_ON_CHESS["Space"])
                        movableList.append((cell_x, cell_y - i))
                    else:
                        break
            elif cells[CELL_COL_CNT * (cell_y - 1) + cell_x].state == CELL_STATE["Nothing"]:
                cells[CELL_COL_CNT * (cell_y - 1) + cell_x].image.fill(CELL_COLOR_BASE_ON_CHESS["Space"])
                if cell_y == 1:
                    cells[CELL_COL_CNT * (cell_y - 1) + cell_x].image.fill(CELL_COLOR_BASE_ON_CHESS["Promotion"])    
                movableList.append((cell_x, cell_y - 1))
            
            # en passant
            if self.en_passant >= 0:
                en_passant_x, en_passant_y = get_cell((existing_chess[enemy_color][self.en_passant].rect.x, existing_chess[enemy_color][self.en_passant].rect.y))
                cells[CELL_COL_CNT * (en_passant_y - 1) + en_passant_x].image.fill(CELL_COLOR_BASE_ON_CHESS["Enemy"])
                movableList.append((en_passant_x, en_passant_y - 1))
            # diagonal direction
            for chess in existing_chess[enemy_color]:
                enemy_x, enemy_y = get_cell((chess.rect.x, chess.rect.y))
                if abs(enemy_x - cell_x) == 1 and cell_y - enemy_y == 1:
                    cells[CELL_COL_CNT * enemy_y + enemy_x].image.fill(CELL_COLOR_BASE_ON_CHESS["Enemy"])
                    movableList.append((enemy_x, enemy_y)) 
             
            return movableList
        # castling hint is for king moval
        if self.chesskind == "King" and castling[teamColor][1] and (cell_x, cell_y) not in enemy_attack:
            leftRook, rightRook = castling[teamColor][0], castling[teamColor][2]

            # check whether other chessman is on the path from leftRook to King 
            for i in range(1, 3):
                if cells[CELL_COL_CNT * (CELL_ROW_CNT - 1) + i].state != CELL_STATE["Nothing"] or (i, CELL_ROW_CNT -1) in enemy_attack:
                    leftRook = False
                    break
            # check whether other chessman is on the path from King to rightRook 
            if CASTLING_MOVE["Long"]["King"] in enemy_attack or CASTLING_MOVE["Long"]["Rook"] in enemy_attack:
                rightRook = False
            for i in range(4, CELL_COL_CNT - 1):
                if cells[CELL_COL_CNT * (CELL_COL_CNT - 1) + i].state != CELL_STATE["Nothing"]:
                    rightRook = False
                    break

            if leftRook:
                # short castling
                cells[(CELL_ROW_CNT - 1) * CELL_COL_CNT + 1].image.fill(CELL_COLOR_BASE_ON_CHESS["Castling"])
                movableList.append((1, CELL_ROW_CNT - 1))
            if rightRook:
                # long castling
                cells[(CELL_ROW_CNT - 1) * CELL_COL_CNT + 5].image.fill(CELL_COLOR_BASE_ON_CHESS["Castling"])
                movableList.append((5,  CELL_ROW_CNT - 1))
        
        # other chessman will use default direction(in constants.py) to move 
        for dir in CHESS_MOVE[self.chesskind]:
            for dir_x, dir_y in dir:
                pos_x, pos_y =  cell_x + dir_x, cell_y + dir_y
                if pos_x < 0 or pos_x >= 8 or pos_y < 0 or pos_y >= 8 or \
                ((pos_x, pos_y) in enemy_attack and self.chesskind == "King"):
                    continue
                
                if cells[pos_y * CELL_COL_CNT + pos_x].state == CELL_STATE["Nothing"]:
                    cells[pos_y * CELL_COL_CNT + pos_x].image.fill(CELL_COLOR_BASE_ON_CHESS["Space"])
                    movableList.append((pos_x, pos_y))
                # Note: when we meet any other chessman in this direction, 
                # we can't go farther anymore => then break
                elif cells[pos_y * CELL_COL_CNT + pos_x].state != self.team:
                    cells[pos_y * CELL_COL_CNT + pos_x].image.fill(CELL_COLOR_BASE_ON_CHESS["Enemy"])
                    movableList.append((pos_x, pos_y))
                    break
                else:
                    break
        return movableList

    # move the chessman to the specific position
    def move(self, cell_x:int, cell_y:int, cells:Sequence["BoardCell"]) -> None:
        origin_cell_x, origin_cell_y = (self.rect.x - INIT_x) // CELL_SIDE_LENGTH, (self.rect.y - INIT_y) // CELL_SIDE_LENGTH
        # recover the cells state to "Nothing"
        cells[origin_cell_x  + origin_cell_y * CELL_COL_CNT].state = CELL_STATE["Nothing"]
        self.rect.x = INIT_x + cell_x * CELL_SIDE_LENGTH + 10
        self.rect.y = INIT_y + cell_y * CELL_SIDE_LENGTH + 10
        # put it down
        self.state = CHESS_STATE["Down"]
        # update the new cell state
        cells[cell_x  + cell_y * CELL_COL_CNT].state = self.team
        recover_boardCell(cells)

def generate_chess_piece(cells:Sequence["BoardCell"], chessman_img:Mapping[str, Mapping[str,"pygame.Surface"]]) -> Tuple["pygame.sprite.Group", Mapping[ str, list["Chesspiece"]]]:
    chess_sprite = pygame.sprite.Group()
    # white team
    order = ["Rook", "Knight", "Bishop", "King","Queen","Bishop","Knight", "Rook"]
    chess = {"Black":[], "White":[]}

    """
    (1) Black "Rook", "Knight", "Bishop", "King","Queen","Bishop","Knight", "Rook"
    (2) Black "Pawn", "Pawn"  , "Pawn"  , "Pawn", "Pawn", "Pawn" , "Pawn" , "Pawn"
    (3) empty row
    (4) empty row
    (5) empty row
    (6) empty row
    (7) White "Pawn", "Pawn"  , "Pawn"  , "Pawn", "Pawn", "Pawn" , "Pawn" , "Pawn"
    (8) White "Rook", "Knight", "Bishop", "King","Queen","Bishop","Knight", "Rook"
    """
    for i, kind in enumerate(order):
        temp = Chesspiece(kind, i, 0, "Black", cells, chessman_img)
        chess_sprite.add(temp)
        chess["Black"].append(temp)

        temp = Chesspiece("Pawn", i, 1, "Black", cells, chessman_img)
        chess_sprite.add(temp)
        chess["Black"].append(temp)
        
        temp = Chesspiece(kind, i, CELL_ROW_CNT-1, "White", cells, chessman_img)
        chess_sprite.add(temp)
        chess["White"].append(temp)

        temp = Chesspiece("Pawn", i, CELL_ROW_CNT-2, "White", cells, chessman_img)
        chess_sprite.add(temp)
        chess["White"].append(temp)

    return chess_sprite, chess
        
# to make next player to observe easily
def flip_board(cells:Sequence["BoardCell"], existing_chess:Mapping[str, Sequence["Chesspiece"]]) -> None:
    for whiteBlackChess in existing_chess:
        for chess in existing_chess[whiteBlackChess]:
            cell_y = (chess.rect.y - INIT_y) // CELL_SIDE_LENGTH
            flip_cell_y = CELL_ROW_CNT - cell_y - 1
            chess.rect.y = flip_cell_y * CELL_SIDE_LENGTH + INIT_y + 10
    for row in range(0, CELL_ROW_CNT // 2):
        for i in range(CELL_COL_CNT):
            cells[CELL_COL_CNT * row + i].state, cells[(CELL_ROW_CNT - row - 1) * CELL_COL_CNT + i].state = cells[(CELL_ROW_CNT - row - 1) * CELL_COL_CNT + i].state, cells[CELL_COL_CNT * row + i].state
    return

def pawn_promotion(pawn:"Chesspiece", chesskind:str, chessman_img:Mapping[str, Mapping[str,"pygame.Surface"]]) -> None:
    pawn.chesskind = chesskind
    del pawn.image
    color = "White" if pawn.team == TEAM["White"] else "Black"

    # change the chessman image 
    pawn.image = pygame.transform.scale(chessman_img[color][chesskind], (CHESS_SIDE_LENGTH, CHESS_SIDE_LENGTH))
    pawn.image.set_colorkey(RED)