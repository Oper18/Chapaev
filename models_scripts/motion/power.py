import bge

controller = bge.logic.getCurrentController()

motion = False

actuator = controller.actuators["Motion"] # the name of the Action actuator

if controller.sensors["Keyboard"].positive: # trigger when buton pressed
    motion = True
    
if motion is True:
    #Set all the properties you want
    actuator.dLoc = [0.01, 0, 0]
    controller.activate(actuator)
    controller.deactivate(actuator)
    motion = False
    
else:
    actuator.dLoc = [0, 0, 0]
    controller.activate(actuator)
    controller.deactivate(actuator)