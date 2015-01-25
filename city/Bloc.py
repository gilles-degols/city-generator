from random import random, randint
from Platform1 import Platform1
from Platform2 import Platform2
from Banc1 import Banc1
from TrashCan import TrashCan
from Banc2 import Banc2
from Banc3 import Banc3

class Bloc(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        self.m_unPosX = un_pos_x
        self.m_unPosY = un_pos_y
        self.m_unPosZ = un_pos_z
        self.m_unSizeX = un_size_x
        self.m_unSizeY = un_size_y
        self.m_listElements = []
        self.m_listPathsMap = [[False for x in range(un_size_y)] for x in range(un_size_x)]
        
        self.buildBloc()
        
    def getPosZ(self):
        return self.m_unPosZ
    
    def buildBloc(self):
        self.division(self.m_unPosX+1, self.m_unPosY+1, self.m_unSizeX-2, self.m_unSizeY-2) # +1 and -2 to create a space around the blocs (buildings not on the edges).
        self.buildPlatform()
        self.buildPaths()
        
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
            for x in range(un_pos_x, un_pos_x + un_size_x):
                self.m_listPathsMap[x][unCutY] = True
            self.m_listPathsMap[un_pos_x - 1][unCutY] = False
            self.m_listPathsMap[un_pos_x + un_size_x][unCutY] = False
            
            for y in range(un_pos_y, un_pos_y + un_size_y):
                self.m_listPathsMap[y][unCutX] = True
            self.m_listPathsMap[unCutX][un_pos_y - 1] = False
            self.m_listPathsMap[unCutX][un_pos_y + un_size_y] = False
            
            self.m_listPathsMap[unCutX][unCutY] = False
            
        elif bCutX:
            unCutX = un_pos_x + randint(1, un_size_x-2)
            self.division(un_pos_x, un_pos_y, unCutX - un_pos_x, un_size_y) # Left
            self.division(unCutX + 1, un_pos_y, un_pos_x + un_size_x - (unCutX + 1), un_size_y) # Right
            
            # Path:
            for y in range(un_pos_y, un_pos_y + un_size_y):
                self.m_listPathsMap[y][unCutX] = True
            self.m_listPathsMap[unCutX][un_pos_y - 1] = False
            self.m_listPathsMap[unCutX][un_pos_y + un_size_y] = False
            
        elif bCutY:
            unCutY = un_pos_y + randint(1, un_size_y-2)
            self.division(un_pos_x, unCutY + 1, un_size_x, un_pos_y + un_size_y - (unCutY + 1)) # Up
            self.division(un_pos_x, un_pos_y, un_size_x, unCutY - un_pos_y) # Down
            
            # Path:
            for x in range(un_pos_x, un_pos_x + un_size_x):
                self.m_listPathsMap[x][unCutY] = True
            self.m_listPathsMap[un_pos_x - 1][unCutY] = False
            self.m_listPathsMap[un_pos_x + un_size_x][unCutY] = False
            
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
    def buildPaths(self):
        for x in range(0, self.m_unSizeX):
            for y in range(0, self.m_unSizeY):
                if self.m_listPathsMap[x][y]:
                    if (self.m_listPathsMap[x-1][y] or self.m_listPathsMap[x+1][y]): # Horizontal path
                        self.buildHorizontalPathElement(x, y)
                    elif (self.m_listPathsMap[x][y-1] or self.m_listPathsMap[x][y+1]): # Vertical path
                        self.buildVerticalPathElement(x, y)
                        
    def buildHorizontalPathElement(self, un_pos_x, un_pos_y):
        fRand = random()
        
        if fRand < 0.125:
            Banc1(un_pos_x, un_pos_y, self.m_unPosZ, 0)
        elif 0.125 <= fRand < 0.25:
            Banc2(un_pos_x, un_pos_y, self.m_unPosZ, 0)
        elif 0.25 <= fRand < 0.375:
            Banc3(un_pos_x, un_pos_y, self.m_unPosZ, 0)
        elif 0.375 <= fRand < 0.5:
            TrashCan(un_pos_x, un_pos_y, self.m_unPosZ, 0)
        
    def buildVerticalPathElement(self, un_pos_x, un_pos_y):
        fRand = random()
        
        if fRand < 0.125:
            Banc1(un_pos_x, un_pos_y, self.m_unPosZ, 3)
        elif 0.125 <= fRand < 0.25:
            Banc2(un_pos_x, un_pos_y, self.m_unPosZ, 3)
        elif 0.25 <= fRand < 0.375:
            Banc3(un_pos_x, un_pos_y, self.m_unPosZ, 3)
        elif 0.375 <= fRand < 0.5:
            TrashCan(un_pos_x, un_pos_y, self.m_unPosZ, 3)
        