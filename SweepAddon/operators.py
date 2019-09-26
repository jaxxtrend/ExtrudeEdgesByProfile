#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bpy
from bpy.types import Operator

# Operator
class SweepOp(bpy.types.Operator):
    bl_idname = "mesh.sweep_by_profile"
    bl_label = "Sweep"
    bl_description = "extrude by profile along the curve"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
   
    def execute(self, context):
        # Здесь будем что-то делать
        i = 0
        while i<4:
            i += 1
            print("We will do something here")
       
        simpletool = context.scene.simpletool
       
        # Например напечатать имя выбранного объекта
        print("For example, print the name of the selected object")
        print(simpletool.profile_obj)
       
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SweepOp)

def unregister():
    bpy.utils.unregister_class(SweepOp)

if __name__ == "__main__":
    register()