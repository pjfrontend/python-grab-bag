import math
import os
import bpy


def set_position(obj, pos):
    x, y, z = pos
    obj.location.x = x
    obj.location.y = y
    obj.location.z = z


def update_position(obj, pos):
    x, y, z = pos
    obj.location.x += x
    obj.location.y += y
    obj.location.z += z


def set_scale(obj, scale):
    x, y, z = scale
    obj.scale.x = x
    obj.scale.y = y
    obj.scale.z = z


def add_text(txt, align_x="CENTER", align_y="CENTER", pos=(0, 0, 0), scale=(1, 1, 1)):
    font_curve = bpy.data.curves.new(type="FONT", name="Font Curve")
    font_curve.body = txt
    obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)
    obj.data.align_x = align_x
    obj.data.align_y = align_y
    bpy.context.scene.collection.objects.link(obj)
    set_position(obj, pos)
    set_scale(obj, scale)
    return obj


def create_world():
    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (
        1,
        1,
        1,
        0.5,
    )
    bpy.context.scene.render.resolution_x = 1280
    bpy.context.scene.render.resolution_y = 720
    bpy.context.scene.render.engine = "BLENDER_WORKBENCH"
    bpy.context.scene.view_settings.view_transform = "Raw"
    bpy.context.scene.render.image_settings.file_format = "FFMPEG"
    bpy.context.scene.render.ffmpeg.format = "MPEG4"


def create_camera(pos=(0, 0, 4)):
    # cam_rotation = (0, math.radians(180), math.radians(180))
    bpy.ops.object.camera_add(location=pos, rotation=(0, 0, 0))
    obj = bpy.data.objects["Camera"]
    obj.data.type = "ORTHO"
    obj.data.ortho_scale = 22
    obj.data.dof.use_dof = True
    obj.data.dof.focus_distance = 30
    return obj


def create_timeline(frame_end):
    bpy.context.scene.frame_current = 0
    bpy.context.scene.frame_end = frame_end


def add_plane(pos, mysize, myname=None, origin_left=True):
    bpy.ops.mesh.primitive_plane_add(
        size=mysize,
        calc_uvs=True,
        enter_editmode=False,
        align="WORLD",
        location=pos,
        rotation=(0, 0, 0),
        # scale=(0, 0, 0),
    )
    current_name = bpy.context.selected_objects[0].name
    obj = bpy.data.objects[current_name]
    if myname is not None:
        obj.name = myname
        obj.data.name = myname + "_mesh"

    if origin_left:
        # moving origin to leftmost
        bpy.ops.object.editmode_toggle()
        bpy.ops.transform.translate(
            value=(mysize / 2, 0, 0),
            orient_type="GLOBAL",
            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
            orient_matrix_type="GLOBAL",
            constraint_axis=(True, False, False),
            mirror=True,
            use_proportional_edit=False,
            proportional_edit_falloff="SMOOTH",
            proportional_size=1,
            use_proportional_connected=False,
            use_proportional_projected=False,
        )
        bpy.ops.object.editmode_toggle()
        bpy.context.active_object.select_set(False)

    return obj


def add_material(obj, material):
    if len(obj.data.materials.items()) != 0:
        obj.data.materials.clear()
    else:
        obj.data.materials.append(material)


def add_lamp():
    # create light datablock, set attributes
    light_data = bpy.data.lights.new(name="light_2.80", type="SUN")
    light_data.energy = 0.5

    # create new object with our light datablock
    light_object = bpy.data.objects.new(name="light_2.80", object_data=light_data)

    # link light object
    bpy.context.collection.objects.link(light_object)

    # make it active
    bpy.context.view_layer.objects.active = light_object

    # change location
    light_object.location = (5, 5, 5)


# clear all existing objects (Cube, Lamp, Camera)
def clear_scene():
    bpy.ops.object.select_all(action="DESELECT")
    for obj in bpy.context.scene.objects:
        obj.select_set(True)

    bpy.ops.object.delete()

    for material in bpy.data.materials:
        bpy.data.materials.remove(material)


def get_material_by_hex_number(hex_tuple):
    material = bpy.data.materials.new("color")
    material.use_nodes = True
    tree = material.node_tree
    nodes = tree.nodes
    bsdf = nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_tuple
    material.diffuse_color = hex_tuple
    return material


def _insert_keyframe(obj, data_path, frame, indexes):
    if indexes is None:
        indexes = [0, 1, 2]

    for i in indexes:
        obj.keyframe_insert(data_path, index=i, frame=frame)


def insert_location_keyframe(obj, frame, indexes=None):
    _insert_keyframe(obj, "location", frame, indexes)


def insert_rotation_keyframe(obj, frame, indexes=None):
    _insert_keyframe(obj, "rotation_euler", frame, indexes)


def insert_scale_keyframe(obj, frame, indexes=None):
    _insert_keyframe(obj, "scale", frame, indexes)


def parent_to_child(a, b):
    b.parent = a
