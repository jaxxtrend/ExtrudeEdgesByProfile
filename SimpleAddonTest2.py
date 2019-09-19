#! /usr/bin/python3
# -*- coding: utf-8 -*-

import bpy
from bpy.types import Panel
from bpy.props import PointerProperty

class SweepOp (bpy.types.Operator):
    bl_idname = "mesh.sweep_by_profile"
    bl_label = "Sweep"
    bl_description = "extrude by prfole along the curve"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    profile_obj: PointerProperty(
                name="Profile_curve",
                type=bpy.types.Object
                )

class SimpleToolPanel (Panel):
    bl_label = "Simpletool"
    bl_idname = "SIMPLE_TOOL"
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
        layout = self.layout
        ob = context.active_object
        scene = bpy.context.scene.objects
        col = layout.column()
        col.operator('mesh.primitive_plane_add', text="Mesh Plane", icon="RNDCURVE")
        col = layout.column()
        col.prop(scene, "Profile_curve", text="Profile")


classes = (
    SimpleToolPanel,
    SweepOp,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()