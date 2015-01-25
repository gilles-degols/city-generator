
class TrapezeBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y, un_height):
        # MULTIPLY COORD BY City.UNIT_VALUE
        # The back:
        # Import Back from Modern 2.blend
        # Move it to (un_pos_x + (un_size_x-1)/2, un_pos_y + un_size_y - 1, un_pos_z)
        obj = bpy.data.objects['_ModernBuidingBack']
		mesh = obj.data
		new_obj = bpy.data.objects.new('ModernBuildingBack', mesh)
		new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City_UNIT_VALUE, (un_pos_y + un_size_y - 1) * City_UNIT_VALUE, un_pos_z * City_UNIT_VALUE)
		
		# Scale it (un_size_x, 1, un_height)
		new_obj.scale = (un_size_x, 1, un_height)
		
		scene.objects.link(new_obj)
        
        # The front windows:
        # Import Window
        # Move it to (un_pos_x + (un_size_x-1)/2, un_pos_y, un_pos_z)
		obj = bpy.data.objects['_ModernBuidingWindow']
		mesh = obj.data
		new_obj = bpy.data.objects.new('ModernBuildingWindow', mesh)
		new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City_UNIT_VALUE, un_pos_y * City_UNIT_VALUE, un_pos_z * City_UNIT_VALUE)
		
        # Scale it (un_size_x, 1, 1)
        new_obj.scale = (un_size_x, 1, 1)
		
		scene.objects.link(new_obj)
		
        unZ = un_pos_z + 1
        unY = un_pos_y + 1/3
        while unZ < un_pos_z + un_height and unY <= un_pos_y + un_size_y - 2:
            # Duplicate last placed object
            # Move it to (un_pos_x + (un_size_x-1)/2, unY, unZ)
			obj = bpy.data.objects['_ModernBuidingWindow']
			mesh = obj.data
			new_obj = bpy.data.objects.new('ModernBuildingWindow', mesh)
			new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City_UNIT_VALUE, unY * City_UNIT_VALUE, unZ * City_UNIT_VALUE)
			
			# Scale it (un_size_x, 1, 1)
			new_obj.scale = (un_size_x, 1, 1)
			
			scene.objects.link(new_obj)
            
			unY += 1/3
            ++unZ
            
        # The center part:
        if un_size_y > 2:
            # Import Center
            # Move it to (un_pos_x + (un_size_x-1)/2, un_pos_y + 1/2 + 1/6, un_pos_z)
			obj = bpy.data.objects['_ModernBuidingCenter']
			mesh = obj.data
			new_obj = bpy.data.objects.new('ModernBuildingCenter', mesh)
			new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City_UNIT_VALUE, (un_pos_y + 1/2 + 1/6) * City_UNIT_VALUE, un_pos_z * City_UNIT_VALUE)
			
			# Scale it (un_size_x, 1, 1)
			new_obj.scale = (un_size_x, 1, 1)
			
			scene.objects.link(new_obj)
            
            unY2 = un_pos_y + 1
            unScaleZ = 2
            while unY2 <= un_pos_y + un_size_y - 10/6:
                # Duplicate last placed Element
                # Move it at (un_pos_x + (un_size_x-1)/2, unY, un_pos_z)
				obj = bpy.data.objects['_ModernBuidingWindow']
				mesh = obj.data
				new_obj = bpy.data.objects.new('ModernBuildingWindow', mesh)
				new_obj.location = ((un_pos_x + (un_size_x-1) / 2) * City_UNIT_VALUE, unY * City_UNIT_VALUE, un_pos_z * City_UNIT_VALUE)
			
                # Scale it (un_size_x, 1, unScaleZ)
				new_obj.scale = (un_size_x, 1, unScaleZ)
				
				scene.objects.link(new_obj)
				
                unScaleZ = min(unScaleZ + 1, unZ - un_pos_z)
                unY2 += 1/3
                
        # Join all objects and remove doubles