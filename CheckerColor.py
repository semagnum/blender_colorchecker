import bpy


class CheckerColor(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Color Name", default="New Color")
    target_color: bpy.props.FloatVectorProperty(
        name="Target Color",
        default=(1.0, 1.0, 1.0),
        min=0.0,
        precision=4,
        subtype='COLOR')
    picked_color: bpy.props.FloatVectorProperty(
        name="Picked Color",
        default=(1.0, 1.0, 1.0),
        min=0.0,
        precision=4,
        subtype="COLOR")
