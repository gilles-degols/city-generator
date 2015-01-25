from random import random, uniform
from city.City import City

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
                
        # Tout joindre et remove doubles.
        scene.objects.active = new_obj
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')