from random import random, randint
from src.platforms.Platform1 import Platform1
from src.platforms.Platform2 import Platform2

class Bloc(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        self.m_unPosX = un_pos_x
        self.m_unPosY = un_pos_y
        self.m_unPosZ = un_pos_z
        self.m_unSizeX = un_size_x
        self.m_unSizeY = un_size_y
        self.m_listElements = []
        self.m_listHorizontalPaths = []
        self.m_listVerticalPaths = []
        
        self.buildBloc()
        
    def getPosZ(self):
        return self.m_unPosZ
    
    def buildBloc(self):
        self.division(self.m_unPosX+1, self.m_unPosY+1, self.m_unSizeX-2, self.m_unSizeY-2) # +1 and -2 to create a space around the blocs (buildings not on the edges).
        self.buildPlatform()
        self.buildHorizontalPaths()
        self.buildVerticalPaths()
        
    def division(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        bCutX = random() > 0.5 and un_size_x > 3
        bCutY = random() > 0.5 and un_size_y > 3
            
        if bCutX and bCutY:
            unCutX = un_pos_x + randint(1, un_size_x-2)
            unCutY = un_pos_y + randint(1, un_size_y-2)
            
            self.division(un_pos_x, unCutY + 1, unCutX - un_pos_x, un_pos_y + un_size_y - (unCutY + 1)) # Upper left
            self.division(unCutX + 1, unCutY + 1, un_pos_x + un_size_x - (unCutX + 1), un_pos_y + un_size_y - (unCutY + 1)) # Upper right
            self.division(unCutX + 1, un_pos_y, un_pos_x + un_size_x - (unCutX + 1), unCutY - un_pos_y) # Lower right
            self.division(un_pos_x, un_pos_y, unCutX - un_pos_x, unCutY - un_pos_y) # Lower left
            
            # Paths:
            self.m_listHorizontalPaths.append((un_pos_x, unCutY, un_size_x, 1))
            self.m_listVerticalPaths.append((unCutX, un_pos_y, 1, un_size_y))
            
        elif bCutX:
            unCutX = un_pos_x + randint(1, un_size_x-2)
            self.division(un_pos_x, un_pos_y, unCutX - un_pos_x, un_size_y) # Left
            self.division(unCutX + 1, un_pos_y, un_pos_x + un_size_x - (unCutX + 1), un_size_y) # Right
            
        elif bCutY:
            unCutY = un_pos_y + randint(1, un_size_y-2)
            self.division(un_pos_x, unCutY + 1, un_size_x, un_pos_y + un_size_y - (unCutY + 1)) # Up
            self.division(un_pos_x, un_pos_y, un_size_x, unCutY - un_pos_y) # Down
            
        else:
            cElement = self.buildElement(un_pos_x, un_pos_y, un_size_x, un_size_y)
            self.m_listElements.append(cElement)
            # TODO Mettre élément en enfant du quartier.
            
    """ To be overriden by inheriting classes to build the elements associated with the bloc type."""
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        pass
    
    """ To be overriden by inheriting classes to build the mountains associated with the bloc type."""
    def buildPlatform(self):        
        if random() < 0.5:
            Platform1(self.m_unPosX, self.m_unPosY, self.m_unPosZ, self.m_unSizeX, self.m_unSizeY)
        else:
            Platform2(self.m_unPosX, self.m_unPosY, self.m_unPosZ, self.m_unSizeX, self.m_unSizeY)
    
    """ To be overriden by inheriting classes to build the paths associated with the bloc type."""
    def buildHorizontalPaths(self):
        pass
    
    """ To be overriden by inheriting classes to build the paths associated with the bloc type."""
    def buildVerticalPaths(self):
        pass