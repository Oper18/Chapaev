import bge
import bpy
import time
import math

bge.render.showMouse(True)

scene = bge.logic.getCurrentScene()

push = False
alpha = 0
power = 0
state = 0
delta = ()
meshArrow = str()
verts = 38
color = 0
red = 0
green = 80
mousePos = [0, 0, 0]
objectPlay = [scene.objects['White_Dice_Board.000'], scene.objects['White_Dice_Board.000'].localPosition]
stay = objectPlay[0].getLinearVelocity()
diceList = {}
diceNum = 0
gamePause = False

def RotationArch():
    global push, alpha, delta, meshArrow
    
    controller = bge.logic.getCurrentController()
    meshArrow = controller.owner.meshes[0]
    
    if controller.sensors["Keyboard"].positive:
        push = True
    
    actuator = controller.actuators["RotArch"]
    
    if push is False:
        controller.sensors["Always"].usePosPulseMode = True
        z = 0.05
        alpha = alpha + 1
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
    global power, state, iter, color, push, alpha, stay, gamePause
    
    if objectPlay[0].getLinearVelocity() != stay:
        gamePause = True
    elif objectPlay[0].getLinearVelocity() == stay:
        gamePause = False
    
    controller = bge.logic.getCurrentController()
    
    actuator = controller.actuators["Motion"]
    
    #point = controller.owner.worldPosition
    point = objectPlay[0].worldPosition
    
    try:
        if controller.sensors["Power"+str(diceNum)].positive:
            state = state + 1
    except KeyError:
        # 39 faces on the arrow
        if state == 1:
            power = power + 0.01
            color = color + 1
            ChangeColor(color)
            
            if power >= 1.9:
                xpower = delta[0] * power
                ypower = delta[1] * power
                objectPlay[0].applyImpulse(point, [xpower, ypower, 0], False)
                power = 0
                state = 0
                #push = False
                #StartColor()
        
        elif state == 2:
            xpower = delta[0] * power
            ypower = delta[1] * power
            objectPlay[0].applyImpulse(point, [xpower, ypower, 0], False)
            power = 0
            state = 0
            #push = False
            #StartColor()
        
def CountCoords(alpha):
    x = 1
    y = 0

    alpha = math.radians(alpha * (180 / 62.5))

    XDelta = x * math.cos(alpha) - y * math.sin(alpha)
    YDelta = x * math.sin(alpha) + y * math.cos(alpha)
    
    return (XDelta, YDelta)

def StartColor():
    global meshArrow
    
    for verts in range(0, 39):
        if verts == 1:
            meshArrow.getVertex(verts,0).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,1).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,2).color = [0.8, 0.8, 0.8, 1]
            #meshArrow.getVertex(verts,3).color = [1, 1, 1, 1]
        
        elif verts == 17:
            meshArrow.getVertex(verts,0).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,1).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,2).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,3).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,4).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,5).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,6).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,7).color = [0.8, 0.8, 0.8, 1]
                
        else:
            meshArrow.getVertex(verts,0).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,1).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,2).color = [0.8, 0.8, 0.8, 1]
            meshArrow.getVertex(verts,3).color = [0.8, 0.8, 0.8, 1]

def ChangeColor(color):
    global meshArrow, verts, red, green
    
    if color % 5 == 0:
        verts = verts - 1
        SetColor()
    
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
        
    if verts == 0:
        verts = 38
        red = 0
        green = 80
        
def SetColor():
    global red, green
    
    if red < 80:
        red = red + 5
        
    elif red == 80 and green > 0:
        green = green - 5
    
def GetCoord():
    global position, diceList, objectPlay, gamePause
    
    controller = bge.logic.getCurrentController()
    object = controller.owner
    diceList[object.name] = [object, object.localPosition]
    for i in diceList.keys():
        if i != 'Cube.001' and diceList[i][1] == diceList['Cube.001'][1]:
            objectPlay = diceList[i]
                
    IsDiceInPlay()
    
def ChooseDice():
    global objectPlay, diceList, diceNum, push
    #print(len(diceList))
    
    if gamePause is False:
        push = False
        StartColor()
    
        controller = bge.logic.getCurrentController()
        
        if controller.sensors["Select"].positive:
            diceNum = diceNum + 1

        diceOnBoard = []
        #print(diceNum)
        for i in diceList:
            diceOnBoard.append(int(i[-1]))
        
        if diceNum == 8:
            diceNum = min(diceOnBoard)
        
        for i in range(len(diceOnBoard)):
            #print(diceNum)
            if diceNum in diceOnBoard:
                break
            else:
                diceNum = diceNum + 1
            
                if diceNum == 8:
                    diceNum = min(diceOnBoard)
        
        diceName = 'White_Dice_Board.00' + str(diceNum)    
        controller = bge.logic.getCurrentController()
        controller.owner.localPosition = diceList[diceName][1]
    
def IsDiceInPlay():
    global diceList, objectPlay, diceNum
    
    listToRemove = []
    
    for i in diceList:
        object = diceList[i][0]
        if object.localPosition[-1] < 0.645:
            listToRemove.append(object.name)
            
    for i in listToRemove:
        objectPlay = [scene.objects['White_Dice_Board.00' + str(diceNum+1)], scene.objects['White_Dice_Board.00' + str(diceNum+1)].localPosition]
        diceList[i][0].endObject()
        diceList.pop(i)