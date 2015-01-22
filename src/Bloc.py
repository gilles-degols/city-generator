from random import random, randint

class Bloc(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        self.m_unPosX = un_pos_x
        self.m_unPosY = un_pos_y
        self.m_unPosZ = un_pos_z
        self.m_unSizeX = un_size_x
        self.m_unSizeY = un_size_y
        self.m_listElements = []
        
        self.buildBloc()
        
    def getPosZ(self):
        return self.m_unPosZ
    
    def buildBloc(self):
        self.division(self, self.m_unPosX+1, self.m_unPosY+1, self.m_unSizeX-2, self.m_unSizeY-2) # +1 and -2 to create a space around the blocs (buildings not on the edges).
        
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
            
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        