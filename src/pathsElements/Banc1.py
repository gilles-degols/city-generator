
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
            new_obj.rotation_euler = (0, 0, math.pi/2)
            
            scene.objects.link(new_obj)
        elif un_orientation == 2:
            # Put banc1 at (un_pos_x, un_pos_y - 1/3, un_pos_z)
            # Rotate it 180 z
            obj = bpy.data.objects['_Bench1']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench1', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, (un_pos_y - 1/3) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, math.pi)
            
            scene.objects.link(new_obj)
        else:
            # Put banc1 at (un_pos_x + 1/3, un_pos_y, un_pos_z)
            # Rotate it 270 z
            obj = bpy.data.objects['_Bench1']
            mesh = obj.data
            new_obj = bpy.data.objects.new('Bench1', mesh)
            new_obj.location = ((un_pos_x + 1/3) * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
            new_obj.rotation_euler = (0, 0, math.pi*3/2)
            
            scene.objects.link(new_obj)