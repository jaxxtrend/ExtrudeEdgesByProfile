# -*- coding: utf-8 -*-

bl_info = {
    "name": "Sweep by profile",
    "author": "JaxxTrend",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D EditMode > Sidebar > Edit Tab",
    "description": "Sweep by profile",
    "wiki_url": "",
    "category": "Mesh",
}
 
import bpy
from . import operators
from . import properties
from . properties import SimpletoolProps

from bpy.types import (
        Panel,
        PropertyGroup,
        AddonPreferences,
        PointerProperty,
        )

# GUI
class VIEW3D_PT_SimpleToolPanel(Panel):
    bl_label = "Simpletool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Create"
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}
   
    @classmethod
    def poll(cls, context):
        ob = bpy.context.active_object
        return (ob and ob.type == 'MESH')
 
    def draw(self, context):
       
        active_object = context.active_object
       
        simpletool = context.scene.simpletool
 
        layout = self.layout
        col = layout.column()
        col.prop(simpletool, "profile_obj")
        col = layout.column()
        col.operator('mesh.sweep_by_profile', text="Sweep") 
 
classes = (
    SimpletoolProps,
    VIEW3D_PT_SimpleToolPanel,
)
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)    
    
    bpy.types.Scene.simpletool = PointerProperty(type=SimpletoolProps)

    operators.register()
    properties.register()
    
 
def unregister():

    operators.unregister()
    properties.unregister()
    
    del bpy.types.Scene.simpletool

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

       
 
if __name__ == "__main__":
    register()