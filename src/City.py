
from random import randint
from Bloc import Bloc
from math import cos,pi,fabs

class City(object):

    def __init__(self, un_size_x, un_size_y, un_bloc_min_size, un_bloc_max_size, un_initial_road_width, map_elevation):
        self.m_unBlocMinSize = un_bloc_min_size
        self.m_unBlocMaxSize = un_bloc_max_size
        self.m_unSizeX = un_size_x
        self.m_unSizeY = un_size_y
        self.m_listBlocs = []
        self.m_mapElevationData = map_elevation
        
        self.division(0, 0, un_size_x, un_size_y, un_initial_road_width)
        
        
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
            unBlocIndex1 = self.division(un_pos_x, un_pos_y, unCutX - un_pos_x, un_size_y, un_road_width - 1) # Left
            unBlocIndex2 = self.division(unCutX + un_road_width, un_pos_y, un_pos_x + un_size_x - (unCutX + un_road_width), un_size_y, un_road_width - 1) # Right
            
            if unBlocIndex1 >= 0 and unBlocIndex2 >= 0 and abs(self.m_listBlocs[unBlocIndex1].getPosZ() - self.m_listBlocs[unBlocIndex1].getPosZ()) < 1:
                self.buildBridge(unBlocIndex1, unBlocIndex2)
            
        elif bCutY:
            unBlocIndex1 = self.division(un_pos_x, unCutY + un_road_width, un_size_x, un_pos_y + un_size_y - (unCutY + un_road_width), un_road_width - 1) # Up
            unBlocIndex2 = self.division(un_pos_x, un_pos_y, un_size_x, unCutY - un_pos_y, un_road_width - 1) # Down
            
            if unBlocIndex1 >= 0 and unBlocIndex2 >= 0 and abs(self.m_listBlocs[unBlocIndex1].getPosZ() - self.m_listBlocs[unBlocIndex1].getPosZ()) < 1:
                self.buildBridge(unBlocIndex1, unBlocIndex2)
                
        else:
            fZ = self.computeZ(un_pos_x, un_pos_y, un_size_x, un_size_y)
            self.m_listBlocs.append(Bloc(un_pos_x, un_pos_y, fZ, un_size_x, un_size_y))
            print "bloc %s pos %s %s %s size %s %s" % (len(self.m_listBlocs), un_pos_x, un_pos_y, fZ, un_size_x, un_size_y)
            return len(self.m_listBlocs)-1
        
        return -1
            
    def computeZ(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        if self.m_mapElevationData["type"] == "cos*cos":
            return self.m_mapElevationData["amplitude"] * cos(2*pi/self.m_mapElevationData["x period"] * un_pos_x) * cos(2*pi/self.m_mapElevationData["y period"] * un_pos_y)
        else:
            return 0
        
    def buildBridge(self, un_bloc_index_1, un_bloc_index_2):
        pass