from src.Bloc import Bloc
from random import random, randint
from src.elements.gardens.Garden import Garden
from src.elements.buildings.StairsBuilding import StairsBuilding
from src.elements.buildings.TrapezeBuilding import TrapezeBuilding
from src.elements.buildings.SphereBuilding import SphereBuilding
from src.elements.stations.Station import Station

class ModernBloc(Bloc):
    TRAPEZE_BUILDING_MIN_HEIGHT = 1
    TRAPEZE_BUILDING_MAX_HEIGHT = 10
    SPHERE_BUILDING_MIN_HEIGHT = 5
    SPHERE_BUILDING_MAX_HEIGHT = 10
    UNDER_CONSTRUCTION_BUILDING_MIN_HEIGHT = 7
    UNDER_CONSTRUCTION_BUILDING_MAX_HEIGHT = 12

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        Bloc.__init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y)
        
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        fRand = random()
        
        if un_size_x >= 4 and un_size_y >= 4:
            if fRand < 1/6:
                return self.buildModernHouse(un_pos_x, un_pos_y, un_size_x, un_size_y)
            elif 2/6 <= fRand < 3/6:
                return self.buildStairsBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            elif 2/6 <= fRand < 3/6:
                return self.buildTrapezeBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            elif 3/6 <= fRand < 4/6:
                return self.buildSphereBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            elif 4/6 <= fRand < 5/6:
                return self.buildUnderConstructionBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            else:
                if (un_size_x >= 8 and un_size_y >= 3) or (un_size_x >= 3 and un_size_y >= 8):
                    if random() < 0.5:
                        return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)
                    else:
                        return self.buildStation(un_pos_x, un_pos_y, un_size_x, un_size_y)
                else:
                    return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)
            
        elif un_size_x >= 2 and un_size_y >= 2:
            if fRand < 1/3:
                return self.buildStairsBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            elif 1/3 <= fRand < 2/3:
                return self.buildTrapezeBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            else:
                return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)
            
        else:
            return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)
        
    def buildGarden(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return Garden(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)
    
    def buildModernHouse(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unX = un_pos_x + (un_size_x - 1)/2
        unY = un_pos_y + (un_size_y - 1)/2
        return ModernHouse(unX, unY, self.m_unPosZ)
    
    def buildUnderconstructionBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unHeight = randint(self.UNDER_CONSTRUCTION_BUILDING_MIN_HEIGHT, self.UNDER_CONSTRUCTION_BUILDING_MAX_HEIGHT)
        return UnderConstructionBuilding(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y, unHeight)
    
    def buildStairsBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return StairsBuilding(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)
    
    def buildTrapezeBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unHeight = randint(self.TRAPEZE_BUILDING_MIN_HEIGHT, min(self.TRAPEZE_BUILDING_MAX_HEIGHT, (un_size_y - 2) * 3 + 1))
        return TrapezeBuilding(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y, unHeight)
    
    def buildSphereBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unX = un_pos_x + (un_size_x - 1)/2
        unY = un_pos_y + (un_size_y - 1)/2
        unHeight = randint(self.SPHERE_BUILDING_MIN_HEIGHT, min(self.SPHERE_BUILDING_MAX_HEIGHT, un_size_x, un_size_y))
        return SphereBuilding(unX, unY, self.m_unPosZ, unHeight)
    
    def buildStation(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return Station(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)