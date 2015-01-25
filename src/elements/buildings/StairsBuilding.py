from random import random

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
            new.obj.rotation_euler = (0, 0, math.pi / 2)
        elif 0.5 <= fRand < 0.75:
            # Put it at (un_pos_x + un_size_x - 0.5, un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE AND rotate 180 degrees z
            new_obj.location = ((un_pos_x + un_size_x - 0.5) * City.UNIT_VALUE, (un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new.obj.rotation_euler = (0, 0, math.pi)
        else:
            # Put it at (un_pos_x - 0.5, un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE AND rotate 270 degrees z
            new_obj.location = ((un_pos_x - 0.5) * City.UNIT_VALUE, (un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new.obj.rotation_euler = (0, 0, math.pi * 3 / 2)
        
        # Scale Element (unScaleX, unScaleY)
        new_obj.scale = (unScaleX, unScaleY, 1)
        --unScaleX
        --unScaleY
        
        scene.objects.link(new_obj)
        
        while unScaleX > 0 and unScaleY > 0:
            # Duplicate last placed element AND move it upwards (City.UNIT_VALUE)
            new_obj.active = True
            bpy.ops.object.duplicate_move(None, (0, 0, City.UNIT_VALUE))
            
            # Scale Element (unScaleX, unScaleY, 1)
            --unScaleX
            --unScaleY
            
            scene.objects.link(new_obj)
            
        # TODO Join all objects and remove doubles