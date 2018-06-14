import bge
import time

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