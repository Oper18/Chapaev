import bge
import time

push = False
alpha = 0

def RotationArch():
    global push, alpha
    
    alpha = alpha + 1
    
    controller = bge.logic.getCurrentController()
    
    if controller.sensors["Keyboard"].positive:
        push = True
    
    actuator = controller.actuators["RotArch"]

    if push is False:
        controller.sensors["Always"].usePosPulseMode = True
        z = 0.1
    else:
        controller.sensors["Always"].usePosPulseMode = False
        z = 0
        
    controller.sensors["Always"].tap = True
    
    if controller.sensors["Always"].status == 1:
        actuator.dRot = [0, 0, z]
        controller.activate(actuator)
        controller.deactivate(actuator)
        
    elif controller.sensors["Always"].status == 3:
        actuator.dRot = [0, 0, 0]
        controller.activate(actuator)
        controller.deactivate(actuator)