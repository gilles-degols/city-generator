
from random import randint

class City(object):
    '''
    classdocs
    '''


    def __init__(self, un_size_x, un_size_y, b_elevation, un_neighbourhood_min_size, un_neighbourhood_max_size):
        self.m_unNeighbourhoodMinSize = un_neighbourhood_min_size
        self.m_unNeighbourhoodMaxSize = un_neighbourhood_max_size
        self.m_bElevation = b_elevation
        self.m_unSizeX = un_size_x
        self.m_unSizeY = un_size_y
        self.m_listNeighbourhoods = []
        
        
    def division(self, un_pos_x, un_pos_y, un_size_x, un_size_y, un_road_width):
        bCutX = False
        bCutY = False
        
        if un_road_width < 1:
            un_road_width = 1
        
        #Check if cut along x axis:
        if un_size_x > self.m_unNeighbourhoodMaxSize and un_size_x >= 2*self.m_unNeighbourhoodMinSize:
            bCutX = True
            unCutX = un_pos_x + self.m_unNeighbourhoodMinSize + randint(0, un_size_x - 2*self.m_unNeighbourhoodMinSize - un_road_width)
        
        #Check if cut along y axis:
        if un_size_y > self.m_unNeighbourhoodMaxSize and un_size_y >= 2*self.m_unNeighbourhoodMinSize:
            bCutY = True
            unCutY = un_pos_y + self.m_unNeighbourhoodMinSize + randint(0, un_size_y - 2*self.m_unNeighbourhoodMinSize - un_road_width)
         
        # Perform the actual cut:
        if bCutX and bCutY:
            self.division(un_pos_x, unCutY + un_road_width, unCutX-un_pos_x, un_pos_y + un_size_y - (unCutY + un_road_width), un_road_width - 1) # Upper left
            self.division(unCutX + un_road_width, unCutY + un_road_width, un_pos_x + un_size_x - (unCutX + un_road_width), un_pos_y + un_size_y - (unCutY + un_road_width), un_road_width - 1) # Upper right
            self.division(unCutX + un_road_width, un_pos_y, un_pos_x + un_size_x - (unCutX + un_road_width), unCutY - un_pos_y, un_road_width - 1) # Lower right
            self.division(un_pos_x, un_pos_y, unCutX - un_pos_x, unCutY - un_pos_y, un_road_width - 1) # Lower left
            
        elif bCutX:
            self.division(un_pos_x, un_pos_y, unCutX - un_pos_x, un_size_y, un_road_width - 1)
            self.division(unCutX + un_road_width, un_pos_y, un_size_x, un_size_y, un_road_width)
            