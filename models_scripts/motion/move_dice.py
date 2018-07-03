from bge import logic
from math import pi, cos, sin, radians

scene = logic.getCurrentScene()
dict_ = logic.globalDict

verts = 38
color = 0
red = 0
green = 80
counter = 0
power = 0

def get_current_obj():
    cont = logic.getCurrentController()
    obj = cont.owner
    return obj


def dice_choice():
    dice = get_current_obj()
    dice_name = dice.name
    dict_["current_dice"] = {'dice': dice_name, 'power': 60, 'angle': 0}


def rotation_angle():
    arrow = get_current_obj()
    rotation = arrow.worldOrientation.to_euler()
    # from euler to degree
    angle = (rotation.z / (2 * pi) * 360)
    print(angle, rotation.z)
    dict_["current_dice"]["angle"] = angle
    return angle


def move_dice():
    global power
    angle = rotation_angle()
    delta = count_cords(angle)
    dice = scene.objects[dict_["current_dice"]["dice"]]
    x = dict_["current_dice"]["power"]
    point = dice.worldPosition
    xpower = delta[0] * power
    ypower = delta[1] * power
    dice.applyImpulse(point, [xpower, ypower, 0], False)


def count_cords(alpha):
    x = 1
    y = 0
    print('before', alpha)
    alpha = radians(alpha)
    print('after', alpha)

    XDelta = x * cos(alpha) - y * sin(alpha)
    YDelta = x * sin(alpha) + y * cos(alpha)
    
    print("x = ", XDelta)
    print("y = ", YDelta)
    
    return (XDelta, YDelta)


def power_call():
    global color, counter, meshArrow, power
    meshArrow = scene.objects["Arrow_2"].meshes[0]
    color += 1
    power += 0.025
    counter += 1
    print(' color_call {} times'.format(counter))
    change_color(color)

def set_default():
    global verts, color, red, green, counter, power, meshArrow
    print('default call')
    verts = 38
    color = 0
    red = 0
    green = 80
    counter = 0
    power = 0
    for i in range(39):
        if i == 17:
            meshArrow.getVertex(i,0).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,1).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,2).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,3).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,4).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,5).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,6).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,7).color = [1, 1,  1, 1]
        if i == 1:
            meshArrow.getVertex(verts,0).color = [1, 1,  1, 1]
            meshArrow.getVertex(verts,1).color = [1, 1,  1, 1]
            meshArrow.getVertex(verts,2).color = [1, 1,  1, 1]
        else:
            meshArrow.getVertex(i,0).color = [1, 1,  1, 1]
#p    meshArrow.getVertex(verts,0).color = [red/100, green/100, 0, 1]
            meshArrow.getVertex(i,1).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,2).color = [1, 1,  1, 1]
            meshArrow.getVertex(i,3).color = [1, 1,  1, 1]
        

def change_color(color):
    global meshArrow, verts
    print('"This is mesh', meshArrow)
    if color % 5 == 0:
        verts = verts - 1
        SetColor()
        print(red/10)
        print(green/10)
    
    if verts == 1:
        meshArrow.getVertex(verts,0).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,1).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,2).color = [red/100, green/100, 0, 1]
        #meshArrow.getVertex(verts,3).color = [1, 1, 1, 1]
        
    elif verts == 17:
        meshArrow.getVertex(verts,0).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,1).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,2).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,3).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,4).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,5).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,6).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,7).color = [red/100, green/100, 0, 1]
            
    else:
        meshArrow.getVertex(verts,0).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,1).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,2).color = [red/100, green/100, 0, 1]
        meshArrow.getVertex(verts,3).color = [red/100, green/100, 0, 1]
        
def SetColor():
    global red, green
    
    if red < 80:
        red = red + 5
        
    elif red == 80 and green > 0:
        green = green - 5
