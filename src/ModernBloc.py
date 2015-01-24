from src.Bloc import Bloc
from random import random, randint
from src.elements.gardens.Garden import Garden
from src.elements.buildings.StairsBuilding import StairsBuilding
from src.elements.buildings.TrapezeBuilding import TrapezeBuilding
from src.elements.buildings.SphereBuilding import SphereBuilding

class ModernBloc(Bloc):
    TRAPEZE_BUILDING_MIN_HEIGHT = 1
    TRAPEZE_BUILDING_MAX_HEIGHT = 10
    SPHERE_BUILDING_MIN_HEIGHT = 5
    SPHERE_BUILDING_MAX_HEIGHT = 10

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        Bloc.__init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y)
        
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        fRand = random()
        
        if un_size_x >= 4 and un_size_y >= 4:
            if fRand < 0.25:
                return self.buildStairsBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            elif 0.25 <= fRand < 0.5:
                return self.buildTrapezeBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
            elif 0.5 <= fRand < 0.75:
                return self.buildSphereBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
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
    
    def buildStairsBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return StairsBuilding(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)
    
    def buildTrapezeBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unHeight = randint(self.TRAPEZE_BUILDING_MIN_HEIGHT, min(self.TRAPEZE_BUILDING_MAX_HEIGHT, (un_size_y - 2) * 3 + 1))
        return TrapezeBuilding(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y, unHeight)
    
    def buildSphereBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unX = un_pos_x + (un_size_x - 1)/2
        unY = un_pos_y + (un_size_y - 1)/2
        unHeight = randint(self.SPHERE_BUILDING_MIN_HEIGHT, min(self.SPHERE_BUILDING_MAX_HEIGHT, un_size_x, un_size_y))
        return SphereBuilding(un_pos_x, un_pos_y, self.m_unPosZ, unHeight)