from random import random

class UnderConstructionBuilding(object):

    def __init__(self, un_pos_x, un_pos_y, un_pos_z, un_size_x, un_size_y, un_height):
        wall = bpy.data.objects['_UnderConstructionElement']
        window = bpy.data.objects['_UnderConstructionWindow']
        linkedBeams = bpy.data.objects['_UnderConstructionLinkedBeams']
        beamPieces = bpy.data.objects['_UnderConstructionBeamPieces']
        
        new_obj = bpy.data.objects.new('UnderConstructionElement', wall.data)
        new_obj.location = ((un_pos_x + (un_size_x - 1)/2) * City.UNIT_VALUE, (un_pos_y + (un_size_y - 1)/2) * City.UNIT_VALUE, un_pos_z * City.UNIT_VALUE)
        new_obj.scale = (un_size_x, un_size_y, 1)
        new_obj.select = True
        scene.objects.link(new_obj)
        
        for i in range(1, un_height - 2):
            new_obj = bpy.data.objects.new('UnderConstructionWindow', window.data)
            new_obj.location = ((un_pos_x + (un_size_x - 1)/2) * City.UNIT_VALUE, (un_pos_y + (un_size_y - 1)/2) * City.UNIT_VALUE, (un_pos_z + i) * City.UNIT_VALUE)
            new_obj.scale = (un_size_x, un_size_y, 1)
            new_obj.select = True
            scene.objects.link(new_obj)
        
        for j in range(un_height - 1, un_height):
            for k in range(un_pos_x, un_size_x - 1):
                for l in range(un_pos_y, un_size_y - 1):
                    new_obj = bpy.data.objects.new('UnderConstructionLinkedBeams', linkedBeams.data)
                    new_obj.location = (k * City.UNIT_VALUE, l * City.UNIT_VALUE, (un_pos_z + j) * City.UNIT_VALUE)
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