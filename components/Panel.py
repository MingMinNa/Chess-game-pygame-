
import pygame
from components import *
from components.chesspiece import *
from components.boardcell import *


# Chessman on the promotion panel
class PanelChess(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, size:int, color:str, chesskind:str, chessman_img:Mapping[str, Mapping[str,"pygame.Surface"]]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(chessman_img[color][chesskind], (CHESS_SideLength, CHESS_SideLength))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Promotion panel
class Panel(pygame.sprite.Sprite):
    def __init__(self, panelSprite: "pygame.sprite.Group", color:str, chessman_img:Mapping[str, Mapping[str,"pygame.Surface"]]) -> None:
        chesskind = ["Queen", "Rook", "Knight", "Bishop"]
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = PANEL_INIT_X
        self.rect.y = PANEL_INIT_Y
        self.chessman = [ PanelChess(170 + (100 * i), 300 , CHESS_SideLength, color, chesskind[i], chessman_img) for i in range(len(chesskind))]
        
