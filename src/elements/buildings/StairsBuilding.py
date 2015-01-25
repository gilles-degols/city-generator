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
            new_obj.rotation_euler = (0, 0, math.pi / 2)
        elif 0.5 <= fRand < 0.75:
            # Put it at (un_pos_x + un_size_x - 0.5, un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE AND rotate 180 degrees z
            new_obj.location = ((un_pos_x + un_size_x - 0.5) * City.UNIT_VALUE, (un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, math.pi)
        else:
            # Put it at (un_pos_x - 0.5, un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE AND rotate 270 degrees z
            new_obj.location = ((un_pos_x - 0.5) * City.UNIT_VALUE, (un_pos_y + un_size_y - 0.5) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, math.pi * 3 / 2)
        
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