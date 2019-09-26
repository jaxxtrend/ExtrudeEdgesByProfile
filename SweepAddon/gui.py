#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bpy
from bpy.types import Panel

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

def register():
    bpy.utils.register_class(VIEW3D_PT_SimpleToolPanel)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_SimpleToolPanel)

if __name__ == "__main__":
    register()