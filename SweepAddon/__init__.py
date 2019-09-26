#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

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

if "bpy" in locals():
    import importlib
    importlib.reload(operators)
    importlib.reload(properties)
    importlib.reload(gui)
    
else:
    
    from . import operators
    from . import properties
    from . import gui

import bpy

def register():
    gui.register()
    operators.register()
    properties.register()


def unregister():
    gui.unregister()
    operators.unregister()
    properties.unregister()

if __name__ == "__main__":
    register()