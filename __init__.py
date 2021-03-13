bl_info = {
    "name": "Color Checker Calibrator",
    "authors": "Spencer Magnusson & Philippe Manzano",
    "version": (0, 2),
    "blender": (2, 80, 0),
    "location": "Image Editor",
    "description": "Generates Node group to calibrate an image to an Andoer color checker",
    "tracker_url": "https://github.com/semagnum/blender_colorchecker/issues",
    "category": "Compositing",
}

import bpy
from .NODE_OT_ColorCheckerMatch import NODE_OT_ColorCheckerMatch
from .NODE_PT_ColorChecker import NODE_PT_ColorChecker

classes = [NODE_OT_ColorCheckerMatch, NODE_PT_ColorChecker]

def register():
    scene = bpy.types.Scene
    scene.colorchecker_001 = bpy.props.FloatVectorProperty(
        default=(0.171,0.084,0.06),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_002 = bpy.props.FloatVectorProperty(
        default=(0.604,0.356,0.266),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_003 = bpy.props.FloatVectorProperty(
        default=(0.13,0.238,0.451),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_004 = bpy.props.FloatVectorProperty(
        default=(0.1,0.153,0.047),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_005 = bpy.props.FloatVectorProperty(
        default=(0.266,0.25,0.539),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_006 = bpy.props.FloatVectorProperty(
        default=(0.231,0.776,0.631),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_007 = bpy.props.FloatVectorProperty(
        default=(0.947,0.181,0.017),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_008 = bpy.props.FloatVectorProperty(
        default=(0.08,0.105,0.468),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_009 = bpy.props.FloatVectorProperty(
        default=(0.73,0.105,0.205),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_010 = bpy.props.FloatVectorProperty(
        default=(0.105,0.05,0.198),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_011 = bpy.props.FloatVectorProperty(
        default=(0.418,0.807,0.105),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_012 = bpy.props.FloatVectorProperty(
        default=(1.0,0.371,0.01),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_013 = bpy.props.FloatVectorProperty(
        default=(0.025,0.04,0.27),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_014 = bpy.props.FloatVectorProperty(
        default=(0.068,0.296,0.082),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_015 = bpy.props.FloatVectorProperty(
        default=(0.451,0.023,0.032),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_016 = bpy.props.FloatVectorProperty(
        default=(0.956,0.761,0.007),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_017 = bpy.props.FloatVectorProperty(
        default=(0.521,0.082,0.352),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_018 = bpy.props.FloatVectorProperty(
        default=(0.002,0.27,0.413),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_019 = bpy.props.FloatVectorProperty(
        default=(0.973,0.973,0.973),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_020 = bpy.props.FloatVectorProperty(
        default=(0.791,0.791,0.791),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_021 = bpy.props.FloatVectorProperty(
        default=(0.578,0.578,0.578),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_022 = bpy.props.FloatVectorProperty(
        default=(0.275,0.275,0.270),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_023 = bpy.props.FloatVectorProperty(
        default=(0.127,0.127,0.127),
        min=0.0,
        precision=4,
        subtype='COLOR')
    scene.colorchecker_024 = bpy.props.FloatVectorProperty(
        default=(0.032,0.032,0.032),
        min=0.0,
        precision=4,
        subtype='COLOR')
    for cls in classes:      
        bpy.utils.register_class(cls)


def unregister():
    scene = bpy.types.Scene
    del scene.colorchecker_001, scene.colorchecker_002, scene.colorchecker_003, \
        scene.colorchecker_004, scene.colorchecker_005, scene.colorchecker_006, \
        scene.colorchecker_007, scene.colorchecker_008, scene.colorchecker_009, \
        scene.colorchecker_010, scene.colorchecker_011, scene.colorchecker_012, \
        scene.colorchecker_013, scene.colorchecker_014, scene.colorchecker_015, \
        scene.colorchecker_016, scene.colorchecker_017, scene.colorchecker_018, \
        scene.colorchecker_019, scene.colorchecker_020, scene.colorchecker_021, \
        scene.colorchecker_022, scene.colorchecker_023, scene.colorchecker_024
    for cls in classes:      
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
