
from random import randint, random
from Bloc import Bloc
from math import cos, pi, sqrt, atan, hypot, floor, degrees
from RetroBloc import RetroBloc
from ModernBloc import ModernBloc
from Bridge import Bridge

class City(object):
    UNIT_VALUE = 3 # 3 meters or blender units per unit

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
            
            if unBlocIndex1 >= 0 and unBlocIndex2 >= 0:
                fZ2 = self.m_listBlocs[unBlocIndex2].getPosZ()
                fZ1 = self.m_listBlocs[unBlocIndex1].getPosZ()
                fCoefficient = abs(fZ2 - fZ1) / un_road_width
                if fCoefficient <= 0.5:
                    self.buildBridge(unCutX, un_pos_y + floor(un_size_y/2), fZ1, degrees(atan((fZ2 - fZ1)/un_road_width)), 0, hypot(fZ2 - fZ1, un_road_width))
            
        elif bCutY:
            unBlocIndex2 = self.division(un_pos_x, unCutY + un_road_width, un_size_x, un_pos_y + un_size_y - (unCutY + un_road_width), un_road_width - 1) # Up
            unBlocIndex1 = self.division(un_pos_x, un_pos_y, un_size_x, unCutY - un_pos_y, un_road_width - 1) # Down
            
            if unBlocIndex1 >= 0 and unBlocIndex2 >= 0:
                fZ2 = self.m_listBlocs[unBlocIndex2].getPosZ()
                fZ1 = self.m_listBlocs[unBlocIndex1].getPosZ()
                fCoefficient = abs(fZ2 - fZ1) / un_road_width
                if fCoefficient <= 0.5:
                    self.buildBridge(un_pos_x + floor(un_size_x/2), unCutY, fZ1, degrees(atan((fZ2 - fZ1)/un_road_width)), 90, hypot(fZ2 - fZ1, un_road_width))
                
        else:
            fZ = self.computeZ(un_pos_x, un_pos_y, un_size_x, un_size_y)
            cBloc = self.buildBloc(un_pos_x, un_pos_y, fZ, un_size_x, un_size_y)
            self.m_listBlocs.append(cBloc)
            print "bloc %s pos %s %s %s size %s %s" % (len(self.m_listBlocs), un_pos_x, un_pos_y, fZ, un_size_x, un_size_y)
            # TODO Mettre le bloc en enfant de la ville
            return len(self.m_listBlocs)-1
        
        return -1
            
    def computeZ(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        if self.m_mapElevationData["type"] == "cos*cos":
            return self.m_mapElevationData["amplitude"] * cos(2*pi/self.m_mapElevationData["x period"] * un_pos_x) * cos(2*pi/self.m_mapElevationData["y period"] * un_pos_y)
        else:
            return 0
        
    def buildBridge(self, un_pos_x, un_pos_y, f_pos_z, f_angle_y, f_angle_z, f_length):
        Bridge(un_pos_x, un_pos_y, f_pos_z, f_angle_y, f_angle_z, f_length)
    
    def buildBloc(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        """ The probability for a bloc to be modern style is decreasing with the distance from the city centre. """
        fCenter = (self.m_unSizeX/2, self.m_unSizeY/2)
        fBlocCenter = (un_pos_x + un_size_x/2, un_pos_y + un_size_y/2)
        fDistance = sqrt(pow(fBlocCenter[0] - fCenter[0], 2) + pow(fBlocCenter[1] - fCenter[1], 2))
        fRatio = fDistance / max(self.m_unSizeX, self.m_unSizeY)
        
        if random() < fRatio: # Create retro style bloc
            return RetroBloc(un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y)
        else:
            return ModernBloc(un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y)
        
        