import bpy
from .NODE_OT_ColorCheckerMatch import NODE_OT_ColorCheckerMatch

class NODE_PT_ColorChecker(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Color Checker Calibration (Andoer chart)"
    bl_idname = "NODE_PT_ColorChecker"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, 'colorchecker_001', text='001')
        layout.prop(context.scene, 'colorchecker_002', text='002')
        layout.prop(context.scene, 'colorchecker_003', text='003')
        layout.prop(context.scene, 'colorchecker_004', text='004')
        layout.prop(context.scene, 'colorchecker_005', text='005')
        layout.prop(context.scene, 'colorchecker_006', text='006')
        layout.prop(context.scene, 'colorchecker_007', text='007')
        layout.prop(context.scene, 'colorchecker_008', text='008')
        layout.prop(context.scene, 'colorchecker_009', text='009')
        layout.prop(context.scene, 'colorchecker_010', text='010')
        layout.prop(context.scene, 'colorchecker_011', text='011')
        layout.prop(context.scene, 'colorchecker_012', text='012')
        layout.prop(context.scene, 'colorchecker_013', text='013')
        layout.prop(context.scene, 'colorchecker_014', text='014')
        layout.prop(context.scene, 'colorchecker_015', text='015')
        layout.prop(context.scene, 'colorchecker_016', text='016')
        layout.prop(context.scene, 'colorchecker_017', text='017')
        layout.prop(context.scene, 'colorchecker_018', text='018')
        layout.prop(context.scene, 'colorchecker_019', text='019')
        layout.prop(context.scene, 'colorchecker_020', text='020')
        layout.prop(context.scene, 'colorchecker_021', text='021')
        layout.prop(context.scene, 'colorchecker_022', text='022')
        layout.prop(context.scene, 'colorchecker_023', text='023')
        layout.prop(context.scene, 'colorchecker_024', text='024')
        layout.operator(NODE_OT_ColorCheckerMatch.bl_idname, text='Generate Node')