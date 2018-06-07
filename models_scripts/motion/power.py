import bge

controller = bge.logic.getCurrentController()

actuator = controller.actuators["Motion"] # the name of the Action actuator

if controller.sensors["Keyboard"].positive: # trigger when buton pressed

    #Set all the properties you want
    actuator.dLoc = [0.01, 0, 0]
    controller.activate(actuator)