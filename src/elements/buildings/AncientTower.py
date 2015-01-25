
class AncientTower(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_height):
        
        # Mettre objet base de la tour à la bonne position (x * City.UNIT_VALUE...)
        obj = bpy.data.objects['_RetroTowerBase']
        mesh = obj.data
        new_obj = bpy.data.objects.new('RetroTowerBase', mesh)
        new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        
        new_obj.select = True
        scene.objects.link(new_obj)
        
        for i in range(1, un_height - 1):
            # Placer objet "level" de la tour à hauteur i * City.UNIT_VALUE
            obj = bpy.data.objects['_RetroTowerLevel']
            mesh = obj.data
            new_obj = bpy.data.objects.new('RetroTowerLevel', mesh)
            new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_pos_z + i) * City.UNIT_VALUE)
            
            new_obj.select = True
            scene.objects.link(new_obj)
            
        # Placer objet "roof" à hauteur (un_height - 1)*City.UNIT_VALUE
        obj = bpy.data.objects['_RetroTowerRoof']
        mesh = obj.data
        new_obj = bpy.data.objects.new('RetroTowerRoof', mesh)
        new_obj.location = (un_pos_x * City.UNIT_VALUE, un_pos_y * City.UNIT_VALUE, (un_pos_z + un_height - 1) * City.UNIT_VALUE)
        
        new_obj.select = True
        scene.objects.link(new_obj)
        
        # Joindre les objets ET remove doubles
        scene.objects.active = new_obj
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.mode_set(mode='OBJECT')