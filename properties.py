
import bpy

from bpy.props import PointerProperty
from bpy.types import PropertyGroup

# Properties
class SimpletoolProps(PropertyGroup):
    profile_obj: PointerProperty(
                 name="Profile_curve",
                 type=bpy.types.Object
                )

def register():
    bpy.utils.register_class(SimpletoolProps)
    bpy.types.Scene.simpletool = PointerProperty(type=SimpletoolProps)

def unregister():
    bpy.utils.unregister_class(SimpletoolProps)
    del bpy.types.Scene.simpletool

# if __name__ == "__main__":
#     register()