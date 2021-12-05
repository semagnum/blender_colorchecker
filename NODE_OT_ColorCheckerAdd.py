import bpy


class NODE_OT_ColorCheckerAdd(bpy.types.Operator):
    """Create a new Mesh Object"""
    bl_idname = "node.colorchecker_add"
    bl_label = "Add a new colors"
    bl_options = {'REGISTER'}

    def execute(self, context):
        cc_draft_color = context.scene.cc_draft_color
        new_color = context.scene.cc_colors.add()
        new_color.name = cc_draft_color.name
        new_color.target_color = cc_draft_color.target_color
        new_color.picked_color = cc_draft_color.target_color
        return {'FINISHED'}