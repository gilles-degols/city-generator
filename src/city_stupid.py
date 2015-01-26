import bpy
import numpy as np
from bpy.props import *

from random import randint, random
from math import *

scene = bpy.context.scene

bpy.types.Scene.city_x = IntProperty(name="X", default=10)
bpy.types.Scene.city_y = IntProperty(name="Y", default=10)
bpy.types.Scene.city_elevation = BoolProperty(name="Enable elevation", default=False)
bpy.types.Scene.district_min = IntProperty(name="District min", default=10)
bpy.types.Scene.district_max = IntProperty(name="District max", default=10)
bpy.types.Scene.streetlight = IntProperty(name="Street light", default=5)
bpy.types.Scene.bench = IntProperty(name="Bench", default=5)
bpy.types.Scene.trash = IntProperty(name="Trash", default=5)



class AncientBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y, un_height):
        # First the side walls:
        wall_element_1 = bpy.data.objects['_RetroBuildingWall']
        for z in range(0, un_height - 1):
            for x in range(un_size_x):
                
                #Wall element 1
                wall_element = bpy.data.objects.new('RetroBuildingWall', wall_element_1.data)    
                wall_element.location = ((un_pos_x + x) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                wall_element.select = True
                scene.objects.link(wall_element)                             
                                        
                #Place Wall Element 1 at (un_pos_x + x, un_pos_y + un_size_y - 1, un_pos_z) AND rotate it 180 degrees z
                wall_element = bpy.data.objects.new('RetroBuildingWall', wall_element_1.data)   
                wall_element.location = ((un_pos_x + x) * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                wall_element.rotation_euler = (0, 0, pi)
                wall_element.select = True
                scene.objects.link(wall_element)                             
            
                
            for y in range(un_size_y):
                # Place Wall Element 1 at (un_pos_x, un_pos_y + y, un_pos_z) AND rotate it 270 degrees z
                wall_element = bpy.data.objects.new('RetroBuildingWall', wall_element_1.data)
                wall_element.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                wall_element.rotation_euler = (0, 0, pi*1.5)
                wall_element.select = True
                scene.objects.link(wall_element)                             
                
                # Place Wall Element 1 at (un_pos_x + un_size_x - 1, un_pos_y + y, un_pos_z) AND rotate it 90 degrees z
                wall_element = bpy.data.objects.new('RetroBuildingWall', wall_element_1.data)
                wall_element.location = ((un_pos_x + un_size_x - 1) * City.UNIT_VALUE, (un_pos_y + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                wall_element.rotation_euler = (0, 0, pi*0.5)
                wall_element.select = True
                scene.objects.link(wall_element)                             
                
        # Then the roof:
        # 4 corners:        
        roof_element_1 = bpy.data.objects.get('_RetroBuildingRoof1')
        roof_element_2 = bpy.data.objects.get('_RetroBuildingRoof2')
        roof_element_3 = bpy.data.objects.get('_RetroBuildingRoof3')
        
        # Place Roof Element 1 at (un_pos_x, un_pos_y, un_height - 1)
        roof_element = bpy.data.objects.new('RetroBuildingRoof1', roof_element_1.data)
        roof_element.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_height - 1) * City.UNIT_VALUE)
        roof_element.select = True
        scene.objects.link(roof_element)                             
                
        # Place Roof Element 1 at (un_pos_x + un_size_x - 1, un_pos_y, un_height - 1) AND rotate it 90 degrees z
        roof_element = bpy.data.objects.new('RetroBuildingRoof1', roof_element_1.data)
        roof_element.location = ((un_pos_x + un_size_x - 1) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_height - 1) * City.UNIT_VALUE)
        roof_element.rotation_euler = (0, 0, pi * 0.5)
        roof_element.select = True
        scene.objects.link(roof_element)                             
        
        # Place Roof Element 1 at (un_pos_x + un_size_x - 1, un_pos_y + un_size_y - 1, un_height - 1) AND rotate it 180 degrees z
        roof_element = bpy.data.objects.new('RetroBuildingRoof1', roof_element_1.data)
        roof_element.location = ((un_pos_x + un_size_x - 1) * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, (un_height - 1) * City.UNIT_VALUE)
        roof_element.rotation_euler = (0, 0, pi)
        roof_element.select = True
        scene.objects.link(roof_element)                             
        
        # Place Roof Element 1 at (un_pos_x, un_pos_y + un_size_y - 1, un_height - 1) AND rotate it 270 degrees z
        roof_element = bpy.data.objects.new('RetroBuildingRoof1', roof_element_1.data)
        roof_element.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, (un_height - 1) * City.UNIT_VALUE)
        roof_element.rotation_euler = (0, 0, pi*1.5)
        roof_element.select = True
        scene.objects.link(roof_element)                             
        
        # The roof sides:
        for x in range(un_size_x - 1):
            
            # Place Roof Element 2 at (un_pos_x + 0.5 + x, un_pos_y, un_pos_z)
            roof_element = bpy.data.objects.new('RetroBuildingRoof2', roof_element_2.data)
            roof_element.location = ((un_pos_x + 0.5 + x) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE) 
            roof_element.select = True
            scene.objects.link(roof_element)                             
        
            # Place Roof Element 2 at (un_pos_x + 0.5 + x, un_pos_y + un_size_y - 1, un_pos_z) AND rotate 180 degrees z
            roof_element = bpy.data.objects.new('RetroBuildingRoof2', roof_element_2.data)
            roof_element.location = ((un_pos_x + 0.5 + x) * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            roof_element.rotation_euler = (0, 0, pi) 
            roof_element.select = True
            scene.objects.link(roof_element)                             
        
            
        for y in range(un_size_y - 1):
            # Place Roof Element 2 at (un_pos_x, un_pos_y + 0.5 + y, un_pos_z) AND rotate 270 degrees z
            roof_element = bpy.data.objects.new('RetroBuildingRoof2', roof_element_2.data)
            roof_element.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + 0.5 + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            roof_element.rotation_euler = (0, 0, pi*1.5)
            roof_element.select = True
            scene.objects.link(roof_element)                             
        
            # Place Roof Element 2 at (un_pos_x + un_size_x - 1, un_pos_y + 0.5 + y, un_pos_z) AND rotate 90 degrees z
            roof_element = bpy.data.objects.new('RetroBuildingRoof2', roof_element_2.data)
            roof_element.location = ((un_pos_x + un_size_x - 1) * City.UNIT_VALUE, (un_pos_y + 0.5 + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE) 
            roof_element.rotation_euler = (0, 0, pi*0.5)
            roof_element.select = True
            scene.objects.link(roof_element)                             
        
        # The roof centre:
        for x in range(un_size_x - 1):
            for y in range(un_size_y - 1):
                # Place Roof Element 3 at (un_pos_x + 0.5 + x, un_pos_y + 0.5 + y, un_pos_z)
                roof_element = bpy.data.objects.new('RetroBuildingRoof3', roof_element_3.data)
                roof_element.location = ((un_pos_x + 0.5 + x) * City.UNIT_VALUE, (un_pos_y + 0.5 + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                roof_element.select = True
                scene.objects.link(roof_element)                             
        
                
        # Joindre les objets ET remove doubles
        scene.objects.active = roof_element
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')

class AncientTower(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_height):
        
        # Mettre objet base de la tour à la bonne position (x * City.UNIT_VALUE...)
        obj = bpy.data.objects['_RetroTowerBase']
        mesh = obj.data
        new_obj = bpy.data.objects.new('RetroTowerBase', mesh)
        new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        new_obj.select = True
        scene.objects.link(new_obj)
        
        for i in range(1, un_height - 1):
            # Placer objet "level" de la tour à hauteur i * City.UNIT_VALUE
            obj = bpy.data.objects['_RetroTowerLevel']
            mesh = obj.data
            new_obj = bpy.data.objects.new('RetroTowerLevel', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_pos_z + i) * City.UNIT_VALUE)
            
            new_obj.select = True
            scene.objects.link(new_obj)
            
        # Placer objet "roof" à hauteur (un_height - 1)*City.UNIT_VALUE
        obj = bpy.data.objects['_RetroTowerRoof']
        mesh = obj.data
        new_obj = bpy.data.objects.new('RetroTowerRoof', mesh)
        new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_pos_z + un_height - 1) * City.UNIT_VALUE)
        
        new_obj.select = True
        scene.objects.link(new_obj)
        
        # Joindre les objets ET remove doubles
        scene.objects.active = new_obj
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')


class Banc1(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_orientation):
        
        if un_orientation == 0:
            # Put banc1 at (un_pos_x, un_pos_y + 1/3, un_pos_z)
            obj = bpy.data.objects['_Bench1']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench1', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            
            scene.objects.link(new_obj)
        elif un_orientation == 1:
            # Put banc1 at (un_pos_x - 1/3, un_pos_y, un_pos_z)
            # Rotate it 90 z
            obj = bpy.data.objects['_Bench1']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench1', mesh)
            new_obj.location = ((un_pos_x - 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi/2)
            
            scene.objects.link(new_obj)
        elif un_orientation == 2:
            # Put banc1 at (un_pos_x, un_pos_y - 1/3, un_pos_z)
            # Rotate it 180 z
            obj = bpy.data.objects['_Bench1']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench1', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y - 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi)
            
            scene.objects.link(new_obj)
        else:
            # Put banc1 at (un_pos_x + 1/3, un_pos_y, un_pos_z)
            # Rotate it 270 z
            obj = bpy.data.objects['_Bench1']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench1', mesh)
            new_obj.location = ((un_pos_x + 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi*3/2)
            
            scene.objects.link(new_obj)
        

class Banc2(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_orientation):
        
        if un_orientation == 0:
            # Put banc1 at (un_pos_x, un_pos_y + 1/3, un_pos_z)
            obj = bpy.data.objects['_Bench2']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench2', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            
            scene.objects.link(new_obj)
        elif un_orientation == 1:
            # Put banc1 at (un_pos_x - 1/3, un_pos_y, un_pos_z)
            # Rotate it 90 z
            obj = bpy.data.objects['_Bench2']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench2', mesh)
            new_obj.location = ((un_pos_x - 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi/2)
            
            scene.objects.link(new_obj)
        elif un_orientation == 2:
            # Put banc1 at (un_pos_x, un_pos_y - 1/3, un_pos_z)
            # Rotate it 180 z
            obj = bpy.data.objects['_Bench2']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench2', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y - 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi)
            
            scene.objects.link(new_obj)
        else:
            # Put banc1 at (un_pos_x + 1/3, un_pos_y, un_pos_z)
            # Rotate it 270 z
            obj = bpy.data.objects['_Bench2']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench2', mesh)
            new_obj.location = ((un_pos_x + 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi*3/2)
            
            scene.objects.link(new_obj)


class Banc3(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_orientation):
        
        if un_orientation == 0:
            # Put banc1 at (un_pos_x, un_pos_y + 1/3, un_pos_z)
            obj = bpy.data.objects['_Bench3']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench3', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            
            scene.objects.link(new_obj)
        elif un_orientation == 1:
            # Put banc1 at (un_pos_x - 1/3, un_pos_y, un_pos_z)
            # Rotate it 90 z
            obj = bpy.data.objects['_Bench3']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench3', mesh)
            new_obj.location = ((un_pos_x - 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi/2)
            
            scene.objects.link(new_obj)
        elif un_orientation == 2:
            # Put banc1 at (un_pos_x, un_pos_y - 1/3, un_pos_z)
            # Rotate it 180 z
            obj = bpy.data.objects['_Bench3']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench3', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y - 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi)
            
            scene.objects.link(new_obj)
        else:
            # Put banc1 at (un_pos_x + 1/3, un_pos_y, un_pos_z)
            # Rotate it 270 z
            obj = bpy.data.objects['_Bench3']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench3', mesh)
            new_obj.location = ((un_pos_x + 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi*3/2)
            
            scene.objects.link(new_obj)

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
                print(y)
                self.m_listPathsMap[y][unCutX] = True
            self.m_listPathsMap[unCutX][un_pos_y - 1] = False
            self.m_listPathsMap[unCutX][un_pos_y + un_size_y] = False
            
        elif bCutY:
            unCutY = un_pos_y + randint(1, un_size_y-2)
            self.division(un_pos_x, unCutY + 1, un_size_x, un_pos_y + un_size_y - (unCutY + 1)) # Up
            self.division(un_pos_x, un_pos_y, un_size_x, unCutY - un_pos_y) # Down
            
            # Path:
            for x in range(un_pos_x, un_pos_x + un_size_x):
                print(x)
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
            
            if unBlocIndex1 >= 0 and unBlocIndex2 >= 0 and abs(self.m_listBlocs[unBlocIndex1].getPosZ() - self.m_listBlocs[unBlocIndex1].getPosZ()) < 1:
                self.buildBridge(unBlocIndex1, unBlocIndex2)
            
        elif bCutY:
            unBlocIndex1 = self.division(un_pos_x, unCutY + un_road_width, un_size_x, un_pos_y + un_size_y - (unCutY + un_road_width), un_road_width - 1) # Up
            unBlocIndex2 = self.division(un_pos_x, un_pos_y, un_size_x, unCutY - un_pos_y, un_road_width - 1) # Down
            
            if unBlocIndex1 >= 0 and unBlocIndex2 >= 0 and abs(self.m_listBlocs[unBlocIndex1].getPosZ() - self.m_listBlocs[unBlocIndex1].getPosZ()) < 1:
                self.buildBridge(unBlocIndex1, unBlocIndex2)
                
        else:
            fZ = self.computeZ(un_pos_x, un_pos_y, un_size_x, un_size_y)
            cBloc = self.buildBloc(un_pos_x, un_pos_y, fZ, un_size_x, un_size_y)
            self.m_listBlocs.append(cBloc)
            #print "bloc %s pos %s %s %s size %s %s" % (len(self.m_listBlocs), un_pos_x, un_pos_y, fZ, un_size_x, un_size_y)
            # TODO Mettre le bloc en enfant de la ville
            return len(self.m_listBlocs)-1
        
        return -1
            
    def computeZ(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        if self.m_mapElevationData["type"] == "cos*cos":
            return self.m_mapElevationData["amplitude"] * cos(2*pi/self.m_mapElevationData["x period"] * un_pos_x) * cos(2*pi/self.m_mapElevationData["y period"] * un_pos_y)
        else:
            return 0
        
    def buildBridge(self, un_bloc_index_1, un_bloc_index_2): # TODO
        pass
    
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
        
        
from random import random, uniform

class Garden(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        
        for x in range(un_pos_x, un_pos_x + un_size_x):
            for y in range(un_pos_y, un_pos_y + un_size_y):
                if random() < 0.33:
                    # Put (duplicate) "banana palm tree (low poly leaves) joined" at (x, y, un_pos_z)
                    obj = bpy.data.objects['_PalmTree']
                    mesh = obj.data
                    new_obj = bpy.data.objects.new('PalmTree', mesh)
                    new_obj.location = (x * City.UNIT_VALUE, y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                    
                    fScale = uniform(0.2, 1)
                    # Scale it at fScale
                    new_obj.scale = (fScale, fScale, fScale)
                    
                    new_obj.select = True
                    scene.objects.link(new_obj)
                    scene.objects.active = new_obj
                
        # Tout joindre et remove doubles.
        
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')


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


class ModernHouse(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z):
        # Put cylinder at (un_pos_x, un_pos_y, un_pos_z)
        obj = bpy.data.objects['_ModernHouse']
        mesh = obj.data
        new_obj = bpy.data.objects.new('ModernHouse', mesh)
        new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        scene.objects.link(new_obj)


class Platform1(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        fX = un_pos_x + (un_size_x - 1)/2
        fY = un_pos_y + (un_size_y - 1)/2
        
        # Put/duplicate mountain1 at (fX, fY, un_pos_z)*City...
        obj = bpy.data.objects['_Mountain1']
        mesh = obj.data
        new_obj = bpy.data.objects.new('Mountain1', mesh)
        new_obj.location = (fX * City.UNIT_VALUE, fY * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        # Scale it (un_size_x, un_size_y, min(un_size_x, un_size_y))
        new_obj.scale = (un_size_x, un_size_y, min(un_size_x, un_size_y))
        
        scene.objects.link(new_obj)


class Platform2(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        fX = un_pos_x + (un_size_x - 1)/2
        fY = un_pos_y + (un_size_y - 1)/2
        
        # Put/duplicate mountain1 at (fX, fY, un_pos_z)*City...
        obj = bpy.data.objects['_Mountain2']
        mesh = obj.data
        new_obj = bpy.data.objects.new('Mountain2', mesh)
        new_obj.location = (fX * City.UNIT_VALUE, fY * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        # Scale it (un_size_x, un_size_y, min(un_size_x, un_size_y))
        new_obj.scale = (un_size_x, un_size_y, min(un_size_x, un_size_y))
        
        scene.objects.link(new_obj)
        


class RetroBloc(Bloc):
    ANCIENT_TOWER_MAX_HEIGHT = 10 # units (3m here)
    ANCIENT_TOWER_MIN_HEIGHT = 2 # units (3m here)
    ANCIENT_BUILDING_MIN_HEIGHT = 2
    ANCIENT_BUILDING_MAX_HEIGHT = 6

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        Bloc.__init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y)

        
    def buildElement(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        fRand = random()
        if fRand < 0.2:
            return self.buildAncientTower(un_pos_x, un_pos_y, un_size_x, un_size_y)
        elif 0.2 <= fRand < 0.8:
            return self.buildAncientBuilding(un_pos_x, un_pos_y, un_size_x, un_size_y)
        else:
            if (un_size_x >= 8 and un_size_y >= 3) or (un_size_x >= 3 and un_size_y >= 8):
                if random() < 0.5:
                    return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)
                else:
                    return self.buildStation(un_pos_x, un_pos_y, un_size_x, un_size_y)
            else:
                return self.buildGarden(un_pos_x, un_pos_y, un_size_x, un_size_y)

    def buildAncientTower(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unHeight = min(self.ANCIENT_TOWER_MAX_HEIGHT, max(self.ANCIENT_TOWER_MIN_HEIGHT, self.m_unSizeX, self.m_unSizeY))
        unX = un_pos_x + floor(un_size_x/2)
        unY = un_pos_y + floor(un_size_y/2)
        return AncientTower(unX, unY, self.m_unPosZ, unHeight)
        
    def buildAncientBuilding(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        unHeight = min(self.ANCIENT_BUILDING_MAX_HEIGHT, max(self.ANCIENT_BUILDING_MIN_HEIGHT, self.m_unSizeX, self.m_unSizeY))
        return AncientBuilding(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y, unHeight)
    
    def buildGarden(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return Garden(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)
    
    def buildStation(self, un_pos_x, un_pos_y, un_size_x, un_size_y):
        return Station(un_pos_x, un_pos_y, self.m_unPosZ, un_size_x, un_size_y)


class SphereBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_height):
        # Put cylinder at (un_pos_x, un_pos_y, un_pos_z)
        obj = bpy.data.objects['_ModernTowerCylinder']
        mesh = obj.data
        new_obj = bpy.data.objects.new('ModernTowerCylinder', mesh)
        new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        # Scale it (1, 1, un_height - 4)
        new_obj.scale = (1, 1, un_height - 4)
        
        new_obj.select = True
        scene.objects.link(new_obj)
        
        # Put sphere at (un_pos_x, un_pos_y, un_pos_z + un_height - 4)
        obj = bpy.data.objects['_ModernTowerSphere']
        mesh = obj.data
        new_obj = bpy.data.objects.new('ModernTowerSphere', mesh)
        new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_pos_z + un_height - 4) * City.UNIT_VALUE)
        
        new_obj.select = True
        scene.objects.link(new_obj)
        
        # Join and remove doubles
        scene.objects.active = new_obj
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')

class StairsBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        unScaleX = un_size_x
        unScaleY = un_size_y
        
        # Duplicate Element from Modern 1 building.
        obj = bpy.data.objects['_ModernStairsBuildingElement']
        mesh = obj.data
        new_obj = bpy.data.objects.new('ModernStairsBuildingElement', mesh)
        
        fRand = random()
        
        if fRand < 0.25:
            # Put it at (un_pos_x - 0.5, un_pos_y - 0.5) * City.UNIT_VALUE
            new_obj.location = ((un_pos_x - 0.5) * City.UNIT_VALUE, (un_pos_y - 0.5) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        elif 0.25 <= fRand < 0.5:
            # Put it at (un_pos_x + un_size_x - 0.5, un_pos_y - 0.5) * City.UNIT_VALUE AND rotate 90 degrees z
            new_obj.location = ((un_pos_x + un_size_x - 0.5) * City.UNIT_VALUE, (un_pos_y - 0.5) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi / 2)
        elif 0.5 <= fRand < 0.75:
            # Put it at (un_pos_x + un_size_x - 0.5, un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE AND rotate 180 degrees z
            new_obj.location = ((un_pos_x + un_size_x - 0.5) * City.UNIT_VALUE, (un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi)
        else:
            # Put it at (un_pos_x - 0.5, un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE AND rotate 270 degrees z
            new_obj.location = ((un_pos_x - 0.5) * City.UNIT_VALUE, (un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi * 3 / 2)
        
        # Scale Element (unScaleX, unScaleY)
        new_obj.scale = (unScaleX, unScaleY, 1)
        --unScaleX
        --unScaleY
        z_tot = 1 + City.UNIT_VALUE
        new_obj.select = True
        scene.objects.link(new_obj)
        
        while unScaleX > 0 and unScaleY > 0:
            
            # Duplicate last placed element AND move it upwards (City.UNIT_VALUE)            
            new_obj = bpy.data.objects.new('ModernStairsBuildingElement', mesh)
            new_obj.location = (0, 0, z_tot)
            new_obj.scale = (unScaleX, unScaleY, 1)
            z_tot += City.UNIT_VALUE
            new_obj.select = True
            scene.objects.link(new_obj)
            
            # Scale Element (unScaleX, unScaleY, 1)
            unScaleX -= 1
            unScaleY -= 1
        
        # Join all objects and remove doubles
        scene.objects.active = new_obj
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')


class Station(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        unX = un_pos_x + (un_size_x - 1)/2
        unY = un_pos_y + (un_size_y - 1)/2
        
        obj = bpy.data.objects['_Ornithopter']
        mesh = obj.data
        new_obj = bpy.data.objects.new('Ornithopter', mesh)
        new_obj.location = (unX * City.UNIT_VALUE, unY * City.UNIT_VALUE, (un_pos_z + 4/3) * City.UNIT_VALUE)
        
        if un_size_x < un_size_y:
            new_obj.rotation_euler = (0, 0, pi / 2)
        
        scene.objects.link(new_obj)

class TrapezeBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y, un_height):
        # MULTIPLY COORD BY City.UNIT_VALUE
        # The front windows:
        # Import Window
        # Move it to (un_pos_x + (un_size_x-1)/2, un_pos_y, un_pos_z)
        obj = bpy.data.objects['_ModernBuildingWindow']
        mesh = obj.data
        new_obj = bpy.data.objects.new('ModernBuildingWindow', mesh)
        new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        # Scale it (un_size_x, 1, 1)
        new_obj.scale = (un_size_x, 1, 1)
        
        new_obj.select = True
        scene.objects.link(new_obj)
        
        unZ = un_pos_z + 1
        unY = un_pos_y + 1/3
        while unZ < un_pos_z + un_height and unY <= un_pos_y + un_size_y - 2:
            # Duplicate last placed object
            # Move it to (un_pos_x + (un_size_x-1)/2, unY, unZ)
            obj = bpy.data.objects['_ModernBuildingWindow']
            mesh = obj.data
            new_obj = bpy.data.objects.new('ModernBuildingWindow', mesh)
            new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City.UNIT_VALUE, unY * City.UNIT_VALUE, unZ * City.UNIT_VALUE)
            
            # Scale it (un_size_x, 1, 1)
            new_obj.scale = (un_size_x, 1, 1)
            
            new_obj.select = True
            scene.objects.link(new_obj)
            
            unY += 1/3
            unZ += 1
          
        # The center part:
        if un_size_y > 2:
            # Import Center
            # Move it to (un_pos_x + (un_size_x-1)/2, un_pos_y + 1/2 + 1/6, un_pos_z)
            obj = bpy.data.objects['_ModernBuildingCenter']
            mesh = obj.data
            new_obj = bpy.data.objects.new('ModernBuildingCenter', mesh)
            new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City.UNIT_VALUE, (un_pos_y + 1/2 + 1/6) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            
            # Scale it (un_size_x, 1, 1)
            new_obj.scale = (un_size_x, 1, 1)
            
            new_obj.select = True
            scene.objects.link(new_obj)
            
            unY2 = un_pos_y + 1
            unScaleZ = 2
            while unY2 <= un_pos_y + un_size_y - 9/6:
                # Duplicate last placed Element
                # Move it at (un_pos_x + (un_size_x-1)/2, unY, un_pos_z)
                obj = bpy.data.objects['_ModernBuildingWindow']
                mesh = obj.data
                new_obj = bpy.data.objects.new('ModernBuildingWindow', mesh)
                new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City.UNIT_VALUE, unY2 * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            
                # Scale it (un_size_x, 1, unScaleZ)
                new_obj.scale = (un_size_x, 1, unScaleZ)
                
                new_obj.select = True
                scene.objects.link(new_obj)
                
                unScaleZ = min(unScaleZ + 1, unZ - un_pos_z)
                unY2 += 1/3
                
        # The back:
        # Import Back from Modern 2.blend
        # Move it to (un_pos_x + (un_size_x-1)/2, un_pos_y + un_size_y - 1, un_pos_z)
        obj = bpy.data.objects['_ModernBuildingBack']
        mesh = obj.data
        new_obj = bpy.data.objects.new('ModernBuildingBack', mesh)
        new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        # Scale it (un_size_x, 1, un_height)
        new_obj.scale = (un_size_x, 1, unZ - un_pos_z)
        
        new_obj.select = True
        scene.objects.link(new_obj)
        
        # Join all objects and remove doubles
        scene.objects.active = new_obj
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
        

class TrashCan(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_orientation):
        
        if un_orientation == 0:
            # Put banc1 at (un_pos_x, un_pos_y + 1/3, un_pos_z)
            obj = bpy.data.objects['_WasteBin']
            mesh = obj.data
            new_obj = bpy.data.objects.new('WasteBin', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            
            scene.objects.link(new_obj)
        elif un_orientation == 1:
            # Put banc1 at (un_pos_x - 1/3, un_pos_y, un_pos_z)
            # Rotate it 90 z
            obj = bpy.data.objects['_WasteBin']
            mesh = obj.data
            new_obj = bpy.data.objects.new('WasteBin', mesh)
            new_obj.location = ((un_pos_x - 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi/2)
            
            scene.objects.link(new_obj)
        elif un_orientation == 2:
            # Put banc1 at (un_pos_x, un_pos_y - 1/3, un_pos_z)
            # Rotate it 180 z
            obj = bpy.data.objects['_WasteBin']
            mesh = obj.data
            new_obj = bpy.data.objects.new('WasteBin', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y - 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi)
            
            scene.objects.link(new_obj)
        else:
            # Put banc1 at (un_pos_x + 1/3, un_pos_y, un_pos_z)
            # Rotate it 270 z
            obj = bpy.data.objects['_WasteBin']
            mesh = obj.data
            new_obj = bpy.data.objects.new('WasteBin', mesh)
            new_obj.location = ((un_pos_x + 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, pi*3/2)
            
            scene.objects.link(new_obj)        
        
class UnderConstuctionBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y, un_height):
        wall = bpy.data.objects['_UnderConstructionElement']
        window = bpy.data.objects['_UnderConstructionWindow']
        linkedBeams = bpy.data.objects['_UnderConstructionLinkedBeams']
        beamPieces = bpy.data.objects['_UnderConstructionBeamPieces']
        
        new_obj = bpy.data.objects.new('UnderConstructionElement', wall.data)
        new_obj.location = ((un_pos_x + (un_size_x - 1)/2) * City_UNIT_VALUE, (un_pos_y + (un_size_y - 1)/2) * City_UNIT_VALUE, un_pos_z * City_UNIT_VALUE)
        new_obj.scale = (un_size_x, un_size_y, 1)
        new_obj.select = True
        scene.objects.link(new_obj)
        
        for i in range(1, un_height - 2):
            new_obj = bpy.data.objects.new('UnderConstructionWindow', window.data)
            new_obj.location = ((un_pos_x + (un_size_x - 1)/2) * City_UNIT_VALUE, (un_pos_y + (un_size_y - 1)/2) * City_UNIT_VALUE, (un_pos_z + i) * City_UNIT_VALUE)
            new_obj.scale = (un_size_x, un_size_y, 1)
            new_obj.select = True
            scene.objects.link(new_obj)
        
        for j in range(un_height-1, un_height):
            for k in range(un_pos_x, un_size_x - 1):
                for l in range(un_pos_y, un_size_y - 1):
                    new_obj = bpy.data.objects.new('UnderConstructionLinkedBeams', linkedBeams.data)
                    new_obj.location = (k * City_UNIT_VALUE, l * City_UNIT_VALUE, (un_pos_z + j) * City_UNIT_VALUE)
                    new_obj.select = True
                    scene.objects.link(new_obj)
            
        # Join all objects and remove doubles
        scene.objects.active = new_obj
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        
class CityDemoPanel(bpy.types.Panel):
    bl_label = "City Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'TestPreAlphaDebug'

    def draw(self, context):
        layout = self.layout
        layout.label(text="City Size:")
        
        scene = context.scene
        row = layout.row()
        row.prop(scene, 'city_x')
        row.prop(scene, 'city_y')
        row = layout.row()
        row.prop(scene, 'city_elevation')
        row = layout.row()
        layout.label(text="District size (min-max)")
        row = layout.row()
        row.prop(scene, 'district_min')
        row.prop(scene, 'district_max')
        row = layout.row()
        layout.label(text="Street Furniture (frequency)")
        row = layout.row()
        row.prop(scene, 'bench')
        row.prop(scene, 'trash')
        row = layout.row()
        row.prop(scene, 'streetlight')
        row = layout.row()
        row.operator('city.generate')
        row.operator('city.delete')

class OBJECT_OT_GenerateCity(bpy.types.Operator):
    bl_idname = "city.generate"
    bl_label = "Generate"
    bl_description = "Generates the city based on the given parameters."
 
    def execute(self, context):
        scene = context.scene
        
        # Remove previous city (if any)
        bpy.ops.city.delete()

        # Add an empty that will serve as the parent of all buildings
        bpy.ops.object.add(type='EMPTY')
        empty = bpy.context.object
        empty.name = 'City'
        
        #Création ville TODO
        cCity = City(20, 15, 3, 10, 3, {"type":"cos*cos", "amplitude":1, "x period":25, "y period":25})

        """
        # Get the template objects (name starting with '_'
        objs = [obj for obj in bpy.data.objects if obj.name[0] == '_']
        
        # Get the mesh from the template object
        meshes = [obj.data for obj in objs]
        
        size = scene.city_x + scene.city_y
        
        # Add the terrain as a plane
        bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0))    # add plane
        floor = bpy.context.object                              # just added object
        floor.name = 'Terrain'                                  # change name
        floor.scale = (size + 2, size + 2, 1)                   # resize
        floor.parent = empty                                    # Link floor to empty
        
        # Create a duplicate linked object of '_Building1'
        for x in np.linspace(-size/2, size/2, size):
            for y in np.linspace(-size/2, size/2, size):

                height = 2 + np.random.rand() * 8                       # Random height
                mesh = meshes[np.random.random_integers(len(meshes))-1] # Random mesh from templates
                new_obj = bpy.data.objects.new('Building.000', mesh)    # Create new object linked to same mesh data
                new_obj.location = (x*2,y*2,0)                          # Set its location
                new_obj.scale = (1,1,height)                            # Set its scale
                scene.objects.link(new_obj)                             # Link new object to scene
                new_obj.parent = empty                                  # Link new object to empty
        """
        return {'FINISHED'}

class OBJECT_OT_DeleteCity(bpy.types.Operator):
    bl_idname = "city.delete"
    bl_label = "Delete"
 
    def execute(self, context):
        scene = context.scene
        
        # Remove previous city
        city = bpy.data.objects.get('City')                         # Get 'City' object
        if not city is None:                                        # If exists
            bpy.ops.object.select_all(action='DESELECT')            # Deselect all
            city.select = True                                      # Select City
            bpy.ops.object.select_hierarchy(direction='CHILD',      # Select all children of City
                                            extend=True)
            bpy.ops.object.delete(use_global=False)                 # Delete selection
    
        return {'FINISHED'}

bpy.utils.register_module(__name__)

