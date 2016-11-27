import bpy
from bpy.types import Menu
global alt, shift, ctrl, key, where

class cactus(Menu):

    bl_label = "Cactus-Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # here, the operators you want (max 8)
        # order in the pie is : right, left, down, up
        pie.operator_enum("mesh.select_mode", "type")   #1  this one has 4 entries (enumeration)
                                                        #2
                                                        #3
                                                        #4
                                                        #5
                                                        #6
                                                        #7
                                                        #8
        
        # To find an operator, right-click on a button or a menu element in blender and "show source".
        # The source code appears in the text editor, the cursor being at the right line.
        # For instance you get : row.operator("render.render", text="Render", icon='RENDER_STILL')
        # Now, copy-paste this line below and change the first word (usually 'row') by 'pie'.
        # Here, you'd get : pie.operator("render.render", text="Render", icon='RENDER_STILL')

# your shortcut's definition :
alt = False
shift = True
ctrl = True
key = "W"
where = "Object Mode"  # --> Object Mode, Mesh, Pose, etc... see Blender pref --> input

def register():
    bpy.utils.register_class(cactus)
    global alt, shift, ctrl, key, where
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name=where)
    kmi = km.keymap_items.new("wm.call_menu_pie", key, "PRESS", alt, shift, ctrl).properties.name="cactus"


def unregister():
    bpy.utils.unregister_class(cactus)


if __name__ == "__main__":
    register()

