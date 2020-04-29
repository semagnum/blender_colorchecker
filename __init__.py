bl_info = {
    "name": "Color Checker Calibrator",
    "author": "Spencer Magnusson",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Image Editor",
    "description": "Generates Node group to calibrate an image to a color checker",
    "tracker_url": "https://github.com/semagnum/blender_colorchecker/issues",
    "category": "Compositing",
}

import bpy
from .NODE_OT_ColorCheckerMatch import NODE_OT_ColorCheckerMatch
from .NODE_PT_ColorChecker import NODE_PT_ColorChecker

classes = [NODE_OT_ColorCheckerMatch, NODE_PT_ColorChecker]

def register():
    scene = bpy.types.Scene
    scene.colorchecker_red = bpy.props.FloatVectorProperty(
        default=(1.0, 0.0, 0.0),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_yellow = bpy.props.FloatVectorProperty(
        default=(1.0, 1.0, 0.0),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_green = bpy.props.FloatVectorProperty(
        default=(0.0, 1.0, 0.0),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_cyan = bpy.props.FloatVectorProperty(
        default=(0.0, 1.0, 1.0),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_blue = bpy.props.FloatVectorProperty(
        default=(0.0, 0.0, 1.0),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_magenta = bpy.props.FloatVectorProperty(
        default=(1.0, 0.0, 1.0),
        min=0.0,
        precision=4,
        subtype='COLOR')
    for cls in classes:      
        bpy.utils.register_class(cls)


def unregister():
    scene = bpy.types.Scene
    del scene.colorchecker_red, scene.colorchecker_yellow, scene.colorchecker_green, \
        scene.colorchecker_cyan, scene.colorchecker_blue, scene.colorchecker_magenta
    for cls in classes:      
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
