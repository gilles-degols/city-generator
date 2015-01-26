import bpy
import numpy as np
from bpy.props import *

from City import City
#from City import City

bpy.types.Scene.city_x = IntProperty(name="X", default=10)
bpy.types.Scene.city_y = IntProperty(name="Y", default=10)
bpy.types.Scene.city_elevation = BoolProperty(name="Enable elevation", default=False)
bpy.types.Scene.district_min = IntProperty(name="District min", default=10)
bpy.types.Scene.district_max = IntProperty(name="District max", default=10)
bpy.types.Scene.streetlight = IntProperty(name="Street light", default=5)
bpy.types.Scene.bench = IntProperty(name="Bench", default=5)
bpy.types.Scene.trash = IntProperty(name="Trash", default=5)

class CityDemoPanel(bpy.types.Panel):
    bl_label = "City Generator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'TestPreAlphaDebug'

    def draw(self, context):
        layout = self.layout
        layout.label(text="City Size:")
        
        scene = context.scene
        row = layout.row()
        row.prop(scene, 'city_x')
        row.prop(scene, 'city_y')
        row = layout.row()
        row.prop(scene, 'city_elevation')
        row = layout.row()
        layout.label(text="District size (min-max)")
        row = layout.row()
        row.prop(scene, 'district_min')
        row.prop(scene, 'district_max')
        row = layout.row()
        layout.label(text="Street Furniture (frequency)")
        row = layout.row()
        row.prop(scene, 'bench')
        row.prop(scene, 'trash')
        row = layout.row()
        row.prop(scene, 'streetlight')
        row = layout.row()
        row.operator('city.generate')
        row.operator('city.delete')

class OBJECT_OT_GenerateCity(bpy.types.Operator):
    bl_idname = "city.generate"
    bl_label = "Generate"
    bl_description = "Generates the city based on the given parameters."
 
    def execute(self, context):
        scene = context.scene
        
        # Remove previous city (if any)
        bpy.ops.city.delete()

        # Add an empty that will serve as the parent of all buildings
        bpy.ops.object.add(type='EMPTY')
        empty = bpy.context.object
        empty.name = 'City'
        
        #Création ville TODO
        cCity = City(25, 20, 5, 13, 3, {"type":"cos*cos", "amplitude":1, "x period":25, "y period":25})

        """
        # Get the template objects (name starting with '_'
        objs = [obj for obj in bpy.data.objects if obj.name[0] == '_']
        
        # Get the mesh from the template object
        meshes = [obj.data for obj in objs]
        
        size = scene.city_x + scene.city_y
        
        # Add the terrain as a plane
        bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0))    # add plane
        floor = bpy.context.object                              # just added object
        floor.name = 'Terrain'                                  # change name
        floor.scale = (size + 2, size + 2, 1)                   # resize
        floor.parent = empty                                    # Link floor to empty
        
        # Create a duplicate linked object of '_Building1'
        for x in np.linspace(-size/2, size/2, size):
            for y in np.linspace(-size/2, size/2, size):

                height = 2 + np.random.rand() * 8                       # Random height
                mesh = meshes[np.random.random_integers(len(meshes))-1] # Random mesh from templates
                new_obj = bpy.data.objects.new('Building.000', mesh)    # Create new object linked to same mesh data
                new_obj.location = (x*2,y*2,0)                          # Set its location
                new_obj.scale = (1,1,height)                            # Set its scale
                scene.objects.link(new_obj)                             # Link new object to scene
                new_obj.parent = empty                                  # Link new object to empty
        """
        return {'FINISHED'}

class OBJECT_OT_DeleteCity(bpy.types.Operator):
    bl_idname = "city.delete"
    bl_label = "Delete"
 
    def execute(self, context):
        scene = context.scene
        
        # Remove previous city
        city = bpy.data.objects.get('City')                         # Get 'City' object
        if not city is None:                                        # If exists
            bpy.ops.object.select_all(action='DESELECT')            # Deselect all
            city.select = True                                      # Select City
            bpy.ops.object.select_hierarchy(direction='CHILD',      # Select all children of City
                                            extend=True)
            bpy.ops.object.delete(use_global=False)                 # Delete selection
    
        return {'FINISHED'}

bpy.utils.register_module(__name__)

