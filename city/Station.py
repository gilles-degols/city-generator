from city.City import City

class Station(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y):
        unX = un_pos_x + (un_size_x - 1)/2
        unY = un_pos_y + (un_size_y - 1)/2
        
        obj = bpy.data.objects['_Ornithopter']
        mesh = obj.data
        new_obj = bpy.data.objects.new('Ornithopter', mesh)
        new_obj.location = (unX * City.UNIT_VALUE, unY * City.UNIT_VALUE, (un_pos_z + 4/3) * City.UNIT_VALUE)
        
        if un_size_x < un_size_y:
            new_obj.rotation_euler = (0, 0, math.pi / 2)
        
        scene.objects.link(new_obj)