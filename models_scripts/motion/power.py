import bge
import bpy
import time
import math

push = False
alpha = 0
power = 0
state = 0
delta = ()
meshArrow = str()

def Motion():
    global power
    
    controller = bge.logic.getCurrentController()

    point = controller.owner.worldPosition
    
    motion = False
    xcoord = power

    actuator = controller.actuators["Motion"] # the name of the Action actuator

    if controller.sensors["Keyboard"].positive: # trigger when buton pressed
        controller.owner.applyImpulse(point, [0.5, 0, 0], False)
        motion = True

def RotationArch():
    global push, alpha, delta, meshArrow
    
    alpha = alpha + 1
    
    controller = bge.logic.getCurrentController()
    meshArrow = controller.owner.meshes[0]
    
    if controller.sensors["Keyboard"].positive:
        push = True
    
    actuator = controller.actuators["RotArch"]

    if push is False:
        controller.sensors["Always"].usePosPulseMode = True
        z = 0.05
    else:
        controller.sensors["Always"].usePosPulseMode = False
        z = 0
    
    # alpha = 62 is analog of 180 degrees rotation when step (z) is 0.05
        
    controller.sensors["Always"].tap = True
    
    if controller.sensors["Always"].status == 1:
        actuator.dRot = [0, 0, z]
        controller.activate(actuator)
        controller.deactivate(actuator)
        
    elif controller.sensors["Always"].status == 3:
        delta = CountCoords(alpha)
        actuator.dRot = [0, 0, 0]
        controller.activate(actuator)
        controller.deactivate(actuator)
        
def Power():
    global power, state, iter
    
    controller = bge.logic.getCurrentController()
    
    actuator = controller.actuators["Motion"]
    
    point = controller.owner.worldPosition
    
    if controller.sensors["Power"].positive:
        state = state + 1
        
    # 39 faces on the arrow
    if state == 1:
        power = power + 0.01
        ChangeColor(power)
        if power >= 1.9:
            xpower = delta[0] * power
            ypower = delta[1] * power
            print(xpower)
            print(ypower)
            controller.owner.applyImpulse(point, [xpower, ypower, 0], False)
            power = 0
            state = 0
    
    elif state == 2:
        xpower = delta[0] * power
        ypower = delta[1] * power
        print(xpower)
        print(ypower)
        controller.owner.applyImpulse(point, [xpower, ypower, 0], False)
        power = 0
        state = 0
        
def CountCoords(alpha):
    x = 1
    y = 0

    alpha = math.radians(alpha * (180 / 63.5))

    XDelta = x * math.cos(alpha) - y * math.sin(alpha)
    YDelta = x * math.sin(alpha) + y * math.cos(alpha)
    
    print("x = ", XDelta)
    print("y = ", YDelta)
    
    return (XDelta, YDelta)

def ChangeColor(power):
    global meshArrow
    
    meshArrow.getVertex(1,0).color = [1, 1, 1, 1]
    meshArrow.getVertex(1,1).color = [1, 1, 1, 1]
    meshArrow.getVertex(1,2).color = [1, 1, 1, 1]
    meshArrow.getVertex(1,3).color = [1, 1, 1, 1]