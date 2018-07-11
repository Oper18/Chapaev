#coding:utf-8

import bge
import bpy

blackDicesList = []
whiteDicesList = []

def ChooseListObjects(objects):
	global blackDicesList, whiteDicesList

	blackDicesList = []
	whiteDicesList = []	

	scene = bge.logic.getCurrentScene()
	#print(scene.objects)
	
	for i in range(len(scene.objects)):
		#print(scene.objects[i])
		if scene.objects[i].name[0:5] == 'Black':
			blackDicesList.append(scene.objects[i])

		elif scene.objects[i].name[0:5] == 'White':
			whiteDicesList.append(scene.objects[i])
	
	print(objects['White_Dice_Board.000'].localPosition)
