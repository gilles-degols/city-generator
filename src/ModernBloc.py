from src.Bloc import Bloc
from random import random
from src.elements.gardens.Garden import Garden

class ModernBloc(Bloc):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        Bloc.__init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y)
        
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        fRand = random()
        
        if fRand < 0.25:
            return self.buildStairsBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
        elif 0.25 <= fRand < 0.5:
            return self.buildTrapezeBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
        elif 0.5 <= fRand < 0.75:
            return self.buildSphereBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
        else:
            return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)
        
        
    def buildGarden(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return Garden(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)
    
    def buildStairsBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return StairsBuilding(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)