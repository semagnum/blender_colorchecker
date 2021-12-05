bl_info = {
    "name": "Color Checker Calibrator",
    "author": "Spencer Magnusson",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "Image Editor",
    "description": "Generates Node group to calibrate an image to a color checker",
    "tracker_url": "https://github.com/semagnum/blender_colorchecker/issues",
    "category": "Compositing",
}

import bpy
from .NODE_OT_ColorCheckerMatch import NODE_OT_ColorCheckerMatch
from .NODE_PT_ColorChecker import NODE_PT_ColorChecker, ColorUIL
from .NODE_OT_ColorCheckerAdd import NODE_OT_ColorCheckerAdd
from .NODE_OT_ColorCheckerDelete import NODE_OT_ColorCheckerDelete
from .CheckerColor import CheckerColor

classes = [CheckerColor, NODE_OT_ColorCheckerMatch, NODE_OT_ColorCheckerDelete, NODE_OT_ColorCheckerAdd, ColorUIL,
           NODE_PT_ColorChecker]

def register():
    scene = bpy.types.Scene
    for cls in classes:
        bpy.utils.register_class(cls)

    scene.cc_colors = bpy.props.CollectionProperty(type=CheckerColor)
    scene.cc_active_color = bpy.props.IntProperty(
        name="Active Color",
        default=0,
        description="Index of active color",
    )

    scene.cc_draft_color = bpy.props.PointerProperty(type=CheckerColor)

    scene.adjust_hue = bpy.props.BoolProperty(name='Adjust Hue',
                                              description='Adjusts color hue based on picked color ' +
                                                          'relative to target color',
                                              default=True,
                                              options=set())

    scene.adjust_sat = bpy.props.BoolProperty(name='Adjust Saturation',
                                              description='Adjusts color saturation based on picked color ' +
                                                          'relative to target color',
                                              default=True,
                                              options=set())


def unregister():
    scene = bpy.types.Scene
    del scene.active_color
    del scene.cc_colors
    del scene.adjust_hue
    del scene.adjust_sat
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
