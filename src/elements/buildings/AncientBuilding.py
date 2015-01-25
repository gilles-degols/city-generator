
class AncientBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y, un_height, empty, scene):
        # First the side walls:
        # MULTIPLIER TOUTES LES COORDONNÉES PAR City.UNIT_VALUE
        un_pos_x *= City.UNIT_VALUE
        un_pos_y *= City.UNIT_VALUE
        un_pos_z *= City.UNIT_VALUE
        wall_element_1 = bpy.data.objects['_RetroBuildingWall']
        for z in range(0, un_height - 1):
            for x in range(un_size_x):
                
                #Wall element 1
                wall_element = bpy.data.objects.new('RetroBuildingWall', wall_element_1.data)    
                wall_element.location = ((un_pos_x + x) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)   
                scene.objects.link(wall_element)                             
                wall_element.parent = empty         
                                        
                #Place Wall Element 1 at (un_pos_x + x, un_pos_y + un_size_y - 1, un_pos_z) AND rotate it 180 degrees z
                wall_element = bpy.data.objects.new('RetroBuildingWall', wall_element_1.data)   
                wall_element.location = ((un_pos_x + x) * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                wall_element.rotation_euler = (0, 0, math.pi)
                scene.objects.link(wall_element)                             
                wall_element.parent = empty                                  
            
                
            for y in range(un_size_y):
                # Place Wall Element 1 at (un_pos_x, un_pos_y + y, un_pos_z) AND rotate it 270 degrees z
                wall_element = bpy.data.objects.new('RetroBuildingWall', wall_element_1.data)
                wall_element.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                wall_element.rotation_euler = (0, 0, math.pi*1.5)
                scene.objects.link(wall_element)                             
                wall_element.parent = empty                                 
                
                # Place Wall Element 1 at (un_pos_x + un_size_x - 1, un_pos_y + y, un_pos_z) AND rotate it 90 degrees z
                wall_element = bpy.data.objects.new('RetroBuildingWall', wall_element_1.data)
                wall_element.location = ((un_pos_x + un_size_x - 1) * City.UNIT_VALUE, (un_pos_y + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                wall_element.rotation_euler = (0, 0, math.pi*0.5)
                scene.objects.link(wall_element)                             
                wall_element.parent = empty                                 
                
        # Then the roof:
        # 4 corners:        
        roof_element_1 = bpy.data.objects.get('_RetroBuildingRoof1')
        roof_element_2 = bpy.data.objects.get('_RetroBuildingRoof2')
        roof_element_3 = bpy.data.objects.get('_RetroBuildingRoof3')
        
        # Place Roof Element 1 at (un_pos_x, un_pos_y, un_height - 1)
        roof_element = bpy.data.objects.new('RetroBuildingRoof1', roof_element_1.data)
        roof_element.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_height - 1) * City.UNIT_VALUE)
        scene.objects.link(roof_element)                             
        roof_element.parent = empty                                 
                
        # Place Roof Element 1 at (un_pos_x + un_size_x - 1, un_pos_y, un_height - 1) AND rotate it 90 degrees z
        roof_element = bpy.data.objects.new('RetroBuildingRoof1', roof_element_1.data)
        roof_element.location = ((un_pos_x + un_size_x - 1) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_height - 1) * City.UNIT_VALUE)
        roof_element.rotation_euler = (0, 0, math.pi * 0.5)
        scene.objects.link(roof_element)                             
        roof_element.parent = empty                                 
        
        # Place Roof Element 1 at (un_pos_x + un_size_x - 1, un_pos_y + un_size_y - 1, un_height - 1) AND rotate it 180 degrees z
        roof_element = bpy.data.objects.new('RetroBuildingRoof1', roof_element_1.data)
        roof_element.location = ((un_pos_x + un_size_x - 1) * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, (un_height - 1) * City.UNIT_VALUE)
        roof_element.rotation_euler = (0, 0, math.pi)
        scene.objects.link(roof_element)                             
        roof_element.parent = empty                                 
        
        # Place Roof Element 1 at (un_pos_x, un_pos_y + un_size_y - 1, un_height - 1) AND rotate it 270 degrees z
        roof_element = bpy.data.objects.new('RetroBuildingRoof1', roof_element_1.data)
        roof_element.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, (un_height - 1) * City.UNIT_VALUE)
        roof_element.rotation_euler = (0, 0, math.pi*1.5)
        scene.objects.link(roof_element)                             
        roof_element.parent = empty                                 
        
        # The roof sides:
        for x in range(un_size_x - 1):
            
            # Place Roof Element 2 at (un_pos_x + 0.5 + x, un_pos_y, un_pos_z)
            roof_element = bpy.data.objects.new('RetroBuildingRoof2', roof_element_2.data)
            roof_element.location = ((un_pos_x + 0.5 + x) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE) 
            scene.objects.link(roof_element)                             
            roof_element.parent = empty                                 
        
            # Place Roof Element 2 at (un_pos_x + 0.5 + x, un_pos_y + un_size_y - 1, un_pos_z) AND rotate 180 degrees z
            roof_element = bpy.data.objects.new('RetroBuildingRoof2', roof_element_2.data)
            roof_element.location = ((un_pos_x + 0.5 + x) * City.UNIT_VALUE, (un_pos_y + un_size_y - 1) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            roof_element.rotation_euler = (0, 0, math.pi) 
            scene.objects.link(roof_element)                             
            roof_element.parent = empty                                 
        
            
        for y in range(un_size_y - 1):
            # Place Roof Element 2 at (un_pos_x, un_pos_y + 0.5 + y, un_pos_z) AND rotate 270 degrees z
            roof_element = bpy.data.objects.new('RetroBuildingRoof2', roof_element_2.data)
            roof_element.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y + 0.5 + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            roof_element.rotation_euler = (0, 0, math.pi*1.5)
            scene.objects.link(roof_element)                             
            roof_element.parent = empty                                 
        
            # Place Roof Element 2 at (un_pos_x + un_size_x - 1, un_pos_y + 0.5 + y, un_pos_z) AND rotate 90 degrees z
            roof_element = bpy.data.objects.new('RetroBuildingRoof2', roof_element_2.data)
            roof_element.location = ((un_pos_x + un_size_x - 1) * City.UNIT_VALUE, (un_pos_y + 0.5 + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE) 
            roof_element.rotation_euler = (0, 0, math.pi*0.5)
            scene.objects.link(roof_element)                             
            roof_element.parent = empty                                 
        
        # The roof centre:
        for x in range(un_size_x - 1):
            for y in range(un_size_y - 1):
                # Place Roof Element 3 at (un_pos_x + 0.5 + x, un_pos_y + 0.5 + y, un_pos_z)
                roof_element = bpy.data.objects.new('RetroBuildingRoof3', roof_element_3.data)
                roof_element.location = ((un_pos_x + 0.5 + x) * City.UNIT_VALUE, (un_pos_y + 0.5 + y) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
                scene.objects.link(roof_element)                             
                roof_element.parent = empty                                 
        
                
        # TODO Joindre les objets ET remove doubles
        # TODO Prendre une aspirine
