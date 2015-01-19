
from random import randint
import Bloc
from math import cos

class City(object):

    def __init__(self, un_size_x, un_size_y, b_elevation, un_bloc_min_size, un_bloc_max_size):
        self.m_unBlocMinSize = un_bloc_min_size
        self.m_unBlocMaxSize = un_bloc_max_size
        self.m_bElevation = b_elevation
        self.m_unSizeX = un_size_x
        self.m_unSizeY = un_size_y
        self.m_listBlocs = []
        self.m_elevationAmplitude = 
        
        
    def division(self, un_pos_x, un_pos_y, un_size_x, un_size_y, un_road_width):
        bCutX = False
        bCutY = False
        
        if un_road_width < 1:
            un_road_width = 1
        
        #Check if cut along x axis:
        if un_size_x > self.m_unBlocMaxSize and un_size_x >= 2*self.m_unBlocMinSize:
            bCutX = True
            unCutX = un_pos_x + self.m_unBlocMinSize + randint(0, un_size_x - 2*self.m_unBlocMinSize - un_road_width)
        
        #Check if cut along y axis:
        if un_size_y > self.m_unBlocMaxSize and un_size_y >= 2*self.m_unBlocMinSize:
            bCutY = True
            unCutY = un_pos_y + self.m_unBlocMinSize + randint(0, un_size_y - 2*self.m_unBlocMinSize - un_road_width)
         
        # Perform the actual cut:
        if bCutX and bCutY:
            self.division(un_pos_x, unCutY + un_road_width, unCutX-un_pos_x, un_pos_y + un_size_y - (unCutY + un_road_width), un_road_width - 1) # Upper left
            self.division(unCutX + un_road_width, unCutY + un_road_width, un_pos_x + un_size_x - (unCutX + un_road_width), un_pos_y + un_size_y - (unCutY + un_road_width), un_road_width - 1) # Upper right
            self.division(unCutX + un_road_width, un_pos_y, un_pos_x + un_size_x - (unCutX + un_road_width), unCutY - un_pos_y, un_road_width - 1) # Lower right
            self.division(un_pos_x, un_pos_y, unCutX - un_pos_x, unCutY - un_pos_y, un_road_width - 1) # Lower left
            
        elif bCutX:
            self.division(un_pos_x, un_pos_y, unCutX - un_pos_x, un_size_y, un_road_width - 1) # Left
            self.division(unCutX + un_road_width, un_pos_y, un_pos_x + un_size_x - (unCutX + un_road_width), un_size_y, un_road_width - 1) # Right
            
        elif bCutY:
            self.division(un_pos_x, unCutY + un_road_width, un_size_x, un_pos_y + un_size_y - (unCutY + un_road_width), un_road_width - 1) # Up
            self.division(un_pos_x, un_pos_y, un_size_x, unCutY - un_pos_y, un_road_width - 1) # Down
            
        else:
            fZ = cos(un_pos_x) * cos(un_pos_y)
            self.m_listBlocs.append(Bloc(un_pos_x, un_pos_y, fZ, un_size_x, un_size_y))
            
            