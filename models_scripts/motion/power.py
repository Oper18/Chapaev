import bge
import time

push = False
alpha = 0

def Motion():
    controller = bge.logic.getCurrentController()
    
    motion = False
    xcoord = 0.01

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