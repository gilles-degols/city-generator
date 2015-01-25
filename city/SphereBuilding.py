from city.City import City

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