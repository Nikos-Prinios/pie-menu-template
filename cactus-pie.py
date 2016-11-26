import bpy
from bpy.types import Menu
global shift, ctrl, key, where

class cactus(Menu):

    bl_label = "Cactus-Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # here, all the operators you want (max 8)
        # order in the pie is : right, left, down, up
        pie.operator_enum("mesh.select_mode", "type")   #1
                                                        #2
                                                        #3
                                                        #4
                                                        #5
                                                        #6
                                                        #7
                                                        #8
                                  

# your shortcut's definition :
shift = True
ctrl = True
key = "W"
where = "Object Mode"  # --> Object Mode, Mesh, Pose, etc... see Blender pref --> input

def register():
    bpy.utils.register_class(cactus)
    global shift, ctrl, key, where
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name=where)
    kmi = km.keymap_items.new("wm.call_menu_pie", key, "PRESS", shift, ctrl).properties.name="cactus"


def unregister():
    bpy.utils.unregister_class(cactus)


if __name__ == "__main__":
    register()

