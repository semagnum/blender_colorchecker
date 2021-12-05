import bpy


class NODE_OT_ColorCheckerDelete(bpy.types.Operator):
    """Create a new Mesh Object"""
    bl_idname = "node.colorchecker_delete"
    bl_label = "Delete a color"
    bl_options = {'REGISTER'}

    index: bpy.props.IntProperty(name="Index", default=-1)

    def execute(self, context):
        if self.index < 0 or self.index >= len(context.scene.cc_colors):
            self.report({'ERROR'}, "Index is not set")
            return {'CANCELLED'}
        context.scene.cc_colors.remove(self.index)
        return {'FINISHED'}