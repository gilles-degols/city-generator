from city.City import City

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