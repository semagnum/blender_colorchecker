import bpy
from .NODE_OT_ColorCheckerMatch import NODE_OT_ColorCheckerMatch
from .NODE_OT_ColorCheckerAdd import NODE_OT_ColorCheckerAdd
from .NODE_OT_ColorCheckerDelete import NODE_OT_ColorCheckerDelete


class ColorUIL(bpy.types.UIList):
    """ """

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, 'name', text="Name")
        layout.prop(item, 'picked_color')
        layout.prop(item, 'target_color')
        op = layout.operator(NODE_OT_ColorCheckerDelete.bl_idname, icon='X', text="")
        op.index = index


class NODE_PT_ColorChecker(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Color Checker Calibration"
    bl_idname = "NODE_PT_ColorChecker"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.template_list("ColorUIL", "", scene, "cc_colors", scene, "cc_active_color", rows=8, columns=4)
        box = layout.box()
        box.prop(scene.cc_draft_color, "name")
        box.prop(scene.cc_draft_color, "target_color")
        box.template_color_picker(scene.cc_draft_color, "target_color")
        box.operator(NODE_OT_ColorCheckerAdd.bl_idname, text="Add Color")
        layout.label(text="Adjust")
        row = layout.row(align=True)
        row.prop(scene, "adjust_hue", text="Hue")
        row.prop(scene, "adjust_sat", text="Saturation")
        layout.operator(NODE_OT_ColorCheckerMatch.bl_idname, text='Generate Node')
