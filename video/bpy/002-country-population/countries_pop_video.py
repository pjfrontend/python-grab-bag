import os
import bpy

################## IMPORTS ###################################
files_names = [
    "../utils.py",
    "../utils_bpy.py",
    "countries_pop.py",
]
# get the current working directory
cwd = bpy.path.abspath("//")
for file_name in files_names:
    file_path = os.path.join(cwd, file_name)
    exec(compile(open(file_path).read(), file_path, "exec"))
#############################################################

data.reverse()
clear_scene()
create_world()
add_lamp()


lsfr = 1
txt_mat = get_material_by_hex_number((0, 0, 0, 1))
range_min = 0.1
range_max = 20
text_or_bar_height = 2


for index, item in enumerate(data):

    # get random number for color
    hex_colour = modulo_html_colors_hex(index)
    hex_tuple = convert_hex_24bit_to_colour_tuple(hex_colour)
    mat = get_material_by_hex_number(hex_tuple)

    # get key value
    key, value = item

    # get range value from domain
    normalised_value = result = convert_domain_to_range(
        value=value,
        domain_max=get_max_value(data),
        domain_min=0,
        range_max=range_max,
        range_min=range_min,
    )

    offset = text_or_bar_height * 2 * index

    txt = add_text(
        "{} - {}".format(key, "{:,}".format(value)),
        align_x="LEFT",
        pos=(0, offset + text_or_bar_height, 0),
    )
    add_material(txt, txt_mat)

    plane = add_plane((0, offset, 0), 1, "MyFloor")
    set_scale(plane, (normalised_value, text_or_bar_height, 1))
    add_material(plane, mat)


# animate the camera from bottom to top
frames_in_sec = 24
duration_in_secs = 4 + len(data) * 2
frame_end = duration_in_secs * frames_in_sec
create_timeline(frame_end)

# add watermark with channel name
watermark = add_text(
    "ChartsVizBiz",
    pos=(0, 0, -10),
)
txt_mat = get_material_by_hex_number((1, 0, 0, 1))
add_material(watermark, txt_mat)

bg = add_plane((-25, 0, -20), 1, "MyFloor")
set_scale(bg, (50, 50, 1))
bg_mat = get_material_by_hex_number((1, 1, 1, 1))
add_material(bg, bg_mat)

cam_pos = (range_max / 2, range_max / 4, range_max / 4)
cam = create_camera(pos=cam_pos)
parent_to_child(cam, watermark)
parent_to_child(cam, bg)

insert_location_keyframe(cam, 2 * frames_in_sec)
update_position(cam, (0, (text_or_bar_height * 2) * (len(data) - 3), 0))
insert_location_keyframe(cam, (duration_in_secs - 2) * frames_in_sec)
