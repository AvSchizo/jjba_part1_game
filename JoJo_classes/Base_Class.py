import pygame
pygame.init()

import json

class baseJoJoClass():

	def __init__(self):

		self.pos = [0, 0]

		self.velocities = {
			"self": [0, 0],
		}

		self.inputButtons = {
			"up": pygame.K_UP,
			"down": pygame.K_DOWN,
			"left": pygame.K_LEFT,
			"right": pygame.K_RIGHT,
		}

		self.inputs = []
		self.buttonsPressed = []
		for i in range(8):
			self.buttonsPressed.append(0)



	def convertInputs(self, returning=False):
		pass



	def updateButtonsPressed(self, returning=False):

		returningList = []

		keyList = self.inputButtons.keys()

		for i in range(len(keyList)):
			if pygame.key.get_pressed()[self.inputButtons[keyList[i]]]:
				returningList.append(1)
			else:
				returningList.append(0)

		if returning:
			return returningList
		else:
			self.buttonsPressed = returningList



	def getSprite(self):

		returnSprites = []

		image = pygame.surface.Surface((100, 100))
		image.fill("blue")
		offset = [0, 0]
		returnSprites.append([image, offset])

		return returnSprites


	def draw(self, stuff):

		class tempCamClass():

			pos = [0, 0]

			def getScaling(self):

				return 1
			

		cam = stuff["camera"]
		scrn = stuff["screen"]


		with open("preferences.json", "r") as f:
			prefs = json.load(f)		
		scaling = cam.getScaling()*prefs["screenSizeScale"]

		for pack in self.getSprite():

			image = pack[0]
			image = pygame.transform.scale(image, (image.get_width()*scaling, image.get_height()*scaling))

			start = [
				scrn.get_width()/2,
				scrn.get_height()/2
			]
			for i in range(2):
				start[i] = start[i] + (cam.pos[i]-self.pos[i]+pack[1][i])*scaling
			rect = image.get_rect(center=start)

			scrn.blit(image, rect)