from src.Bloc import Bloc
from random import random
from src.elements.buildings import AncientTower
from math import floor

class RetroBloc(Bloc):
    ANCIENT_TOWER_MAX_HEIGHT = 10 # units (3m here)

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        Bloc.__init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y)

        
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        if random < 0.2:
            self.buildAncientTower(un_pos_x, un_pos_y, un_size_x, un_size_y)
        else:
            self.buildAncientBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            

    def buildAncientTower(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unHeight = min(self.ANCIENT_TOWER_MAX_HEIGHT, max(self.m_unSizeX, self.m_unSizeY))
        unX = un_pos_x + floor(un_size_x/2)
        unY = un_pos_y + floor(un_size_y/2)
        AncientTower(unX, unY, self.m_unPosZ, unHeight)
        
    def buildAncientBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        