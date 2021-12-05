import bpy


def hue_y(x, h):
    norm = abs(h - x)
    cyclic = 1 - norm
    if norm < cyclic:
        return norm + 0.5
    return -1 * cyclic + 0.5


# derived from Blender's C++ version
def rgb_to_hsv(rgb):
    cmax = max(rgb)
    cmin = min(rgb)
    cdelta = cmax - cmin

    v = cmax

    if cmax != 0.0:
        s = cdelta / cmax
    else:
        s = 0.0
        h = 0.0

    if s == 0.0:
        h = 0.0
    else:
        c = tuple(map(lambda i, j: i - j, (cmax, cmax, cmax), rgb))
        c = tuple(col / cdelta for col in c)

        if rgb[0] == cmax:
            h = c[2] - c[1]
        elif rgb[1] == cmax:
            h = 2.0 + c[0] - c[2]
        else:
            h = 4.0 + c[1] - c[0]

        h /= 6.0

        if (h < 0.0):
            h += 1.0

    return (h, s, v)


def adjust_point_list(point_list, num_points):
    while len(point_list) > num_points:
        p = point_list[0]
        point_list.remove(p)

    while len(point_list) < num_points:
        point_list.new(0.0, 0.0)


class NODE_OT_ColorCheckerMatch(bpy.types.Operator):
    """Create a new Mesh Object"""
    bl_idname = "node.colorchecker_match"
    bl_label = "Match Color Checker Colors"
    bl_options = {'REGISTER'}

    def execute(self, context):
        scene = context.scene
        scene.use_nodes = True
        tree = context.scene.node_tree

        adjust_hue = scene.adjust_hue
        adjust_sat = scene.adjust_sat

        if len(scene.cc_colors) == 0:
            self.report({'ERROR'}, "Must have at least one color!")
            return {'CANCELLED'}

        hue_node = tree.nodes.new(type='CompositorNodeHueCorrect')
        hue_node.mapping.use_clip = False

        # add red at both ends to make it cyclic
        colorchecker_rgb = [c for key, c in scene.cc_colors.items()]
        picked_rgb = [c.picked_color for c in colorchecker_rgb]
        target_rgb = [c.target_color for c in colorchecker_rgb]

        picked_hsv = list(map(rgb_to_hsv, picked_rgb))
        target_hsv = list(map(rgb_to_hsv, target_rgb))

        # plot hue points
        picked_h = [hsv[0] for hsv in picked_hsv]
        target_h = [hsv[0] for hsv in target_hsv]

        if any([s == 0 for _, s, _ in picked_hsv]) or any([s == 0 for _, s, _ in target_hsv]):
            self.report({'ERROR'}, "All hue colors must have saturation greater than 0")
            return {'CANCELLED'}

        # HUE
        if adjust_hue:
            hh_points = hue_node.mapping.curves[0].points

            adjust_point_list(hh_points, len(colorchecker_rgb))

            for index, hues in enumerate(zip(picked_h, target_h)):
                picked, target = hues
                hh_points[index].location = (target, hue_y(target, picked))

            # add first point again after 1.0 to make it cyclic
            first_x, first_y = hh_points[0].location
            hh_points.new(first_x + 1.0, first_y)

        # SATURATION
        if adjust_sat:
            picked_s = [((1.0 / s) / 2.0) for _, s, _ in picked_hsv]
            target_s = [((1.0 / s) / 2.0) for _, s, _ in target_hsv]

            hs_points = hue_node.mapping.curves[1].points
            adjust_point_list(hs_points, len(colorchecker_rgb))

            for index, sats in enumerate(zip(picked_s, target_s, target_h)):
                picked, target, x_h = sats
                hs_points[index].location = (x_h, hue_y(target, picked))

        hue_node.mapping.update()

        # add point at the end if needed to match the first point (since it's cyclic)
        if adjust_hue and hue_node.mapping.curves[0].points[-1].location[0] < 1.0:
            hh_points = hue_node.mapping.curves[0].points
            first_x, first_y = hh_points[0].location
            hh_points.new(first_x + 1.0, first_y)
        if adjust_sat and hue_node.mapping.curves[1].points[-1].location[0] < 1.0:
            hs_points = hue_node.mapping.curves[1].points
            first_x, first_y = hs_points[0].location
            hs_points.new(first_x + 1.0, first_y)
        if any([adjust_hue, adjust_sat]):
            hue_node.mapping.update()

        return {'FINISHED'}
