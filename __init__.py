import bpy
from bpy.types import Menu


class cactus(Menu):

    bl_label = "Cactus-Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator_enum("mesh.select_mode", "type")


def register():
    bpy.utils.register_class(cactus)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Mesh")
    kmi = km.keymap_items.new("wm.call_menu_pie", "W", "PRESS", shift=True, ctrl=True).properties.name="cactus"


def unregister():
    bpy.utils.unregister_class(cactus)


if __name__ == "__main__":
    register()

