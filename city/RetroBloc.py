from Bloc import Bloc
from random import random
from AncientTower import AncientTower
from AncientBuilding import AncientBuilding
from Garden import Garden
from math import floor
from Station import Station

class RetroBloc(Bloc):
    ANCIENT_TOWER_MAX_HEIGHT = 10 # units (3m here)
    ANCIENT_TOWER_MIN_HEIGHT = 2 # units (3m here)
    ANCIENT_BUILDING_MIN_HEIGHT = 2
    ANCIENT_BUILDING_MAX_HEIGHT = 6

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        self.m_unPosX = un_pos_x
        self.m_unPosY = un_pos_y
        self.m_unPosZ = un_pos_z
        self.m_unSizeX = un_size_x
        self.m_unSizeY = un_size_y
        self.m_listElements = []
        self.m_listPathsMap = [[False for x in range(un_size_y)] for x in range(un_size_x)]
        
        self.buildBloc()

        
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        fRand = random()
        if fRand < 0.2:
            return self.buildAncientTower(un_pos_x, un_pos_y, un_size_x, un_size_y)
        elif 0.2 <= fRand < 0.8:
            return self.buildAncientBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
        else:
            if (un_size_x >= 8 and un_size_y >= 3) or (un_size_x >= 3 and un_size_y >= 8):
                if random() < 0.5:
                    return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)
                else:
                    return self.buildStation(un_pos_x, un_pos_y, un_size_x, un_size_y)
            else:
                return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)

    def buildAncientTower(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unHeight = min(self.ANCIENT_TOWER_MAX_HEIGHT, max(self.ANCIENT_TOWER_MIN_HEIGHT, self.m_unSizeX, self.m_unSizeY))
        unX = un_pos_x + floor(un_size_x/2)
        unY = un_pos_y + floor(un_size_y/2)
        return AncientTower(unX, unY, self.m_unPosZ, unHeight)
        
    def buildAncientBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unHeight = min(self.ANCIENT_BUILDING_MAX_HEIGHT, max(self.ANCIENT_BUILDING_MIN_HEIGHT, self.m_unSizeX, self.m_unSizeY))
        return AncientBuilding(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y, unHeight)
    
    def buildGarden(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return Garden(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)
    
    def buildStation(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return Station(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)