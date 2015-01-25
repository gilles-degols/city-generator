
class ModernHouse(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z):
        # Put cylinder at (un_pos_x, un_pos_y, un_pos_z)
        obj = bpy.data.objects['_ModernHouse']
        mesh = obj.data
        new_obj = bpy.data.objects.new('ModernHouse', mesh)
        new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        scene.objects.link(new_obj)