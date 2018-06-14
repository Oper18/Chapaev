import bge
import time

push = False
alpha = 0
power = 0
state = False

def Motion():
    global power, state
    
    controller = bge.logic.getCurrentController()
    
    motion = False
    xcoord = power
    print(power)
    actuator = controller.actuators["Motion"] # the name of the Action actuator

    if controller.sensors["Keyboard"].positive: # trigger when buton pressed
        motion = True

    if motion is True:
        #print("True")
        actuator.dLoc = [xcoord, 0, 0]
        controller.activate(actuator)
        controller.deactivate(actuator)
        motion = False
        
    else:
        #print("False")
        actuator.dLoc = [0, 0, 0]
        controller.activate(actuator)
        controller.deactivate(actuator)
        power = 0
        state = False

def RotationArch():
    global push, alpha
    
    alpha = alpha + 1
    
    controller = bge.logic.getCurrentController()
    
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
        actuator.dRot = [0, 0, 0]
        controller.activate(actuator)
        controller.deactivate(actuator)
        
def Power():
    global power, state
    
    controller = bge.logic.getCurrentController()
    
    actuator = controller.actuators["Motion"]
    
    if controller.sensors["Power"].positive:
        state = True
        
    if state is True:
        power = power + 0.01
        if power >= 1.8:
            actuator.dLoc = [power, 0, 0]
            controller.activate(actuator)
            controller.deactivate(actuator)
            power = 0
            state = False
    
    elif state is False:
        actuator.dLoc = [0, 0, 0]
        controller.activate(actuator)
        controller.deactivate(actuator)