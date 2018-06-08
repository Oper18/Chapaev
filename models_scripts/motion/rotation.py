import bge
import time

def RotationArch():
    controller = bge.logic.getCurrentController()
    
    actuator = controller.actuators["RotArch"]
    
    z = 0.1
    
    controller.sensors["Always"].tap = True
    
    if controller.sensors["Always"].status == 1:
        actuator.dRot = [0, 0, z]
        controller.activate(actuator)