from bge import logic
from math import pi, cos

scene = logic.getCurrentScene()
dict_ = logic.globalDict


def get_current_obj():
    cont = logic.getCurrentController()
    obj = cont.owner
    return obj


def dice_choice():
    dice = get_current_obj()
    dice_name = dice.name
    dict_["current_dice"] = {'dice': dice_name, 'power': 60, 'angle': 0}


def rotation_angle():
    rotation = get_current_obj().worldOrientation.to_euler()
    # from euler to degree
    angle = (rotation.z / (2 * pi) * 360)
    dict_["current_dice"]["angle"] = angle
    return angle
    print(dict_["current_dice"])

def move_dice():
    angle = rotation_angle()
    dice = scene.objects[dict_["current_dice"]["dice"]]
    x = dict_["current_dice"]["power"]
    y = abs(cos(angle)) * x
    if angle < 0:
        y = -y
    if abs(angle) > 90:
        x = -x
    print(x, y, 0)
    dice.applyForce([x, y, 0])
