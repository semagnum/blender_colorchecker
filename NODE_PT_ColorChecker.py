import bpy
from .NODE_OT_ColorCheckerMatch import NODE_OT_ColorCheckerMatch

class NODE_PT_ColorChecker(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Color Checker Calibration"
    bl_idname = "NODE_PT_ColorChecker"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, 'colorchecker_red', text='Red')
        layout.prop(context.scene, 'colorchecker_yellow', text='Yellow')
        layout.prop(context.scene, 'colorchecker_green', text='Green')
        layout.prop(context.scene, 'colorchecker_cyan', text='Cyan')
        layout.prop(context.scene, 'colorchecker_blue', text='Blue')
        layout.prop(context.scene, 'colorchecker_magenta', text='Magenta')
        layout.operator(NODE_OT_ColorCheckerMatch.bl_idname, text='Generate Node')