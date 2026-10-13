import pygame
pygame.init()

import json

class baseJoJoClass():

	def __init__(self, globals, inputs=[]):

		self.bg = globals

		self.pos = [0, 0]

		self.velocities = {
			"self": [0, 0],
		}

		self.inputButtons = {
			"right": pygame.K_RIGHT,
			"left": pygame.K_LEFT,
			"up": pygame.K_UP,
			"down": pygame.K_DOWN,
		}

		self.totalInputs = inputs

		self.direction = 1
		self.stun = 0



	def moveForVel(self, distance, direction):
		rep = abs(round(distance))
		for i in range(reps):
			lastPos = self.pos[direction]
			self.pos[direction] += round(distance)/reps
			if self.touchingMapGeo():
				self.pos[direction] = lastPos
				self.velocities["self"][direction] = 0



	def convertInputs(self, returning=False):

		allKeysPressed = pygame.key.get_pressed()
		keysPressed = []
		for act in [self.inputButtons[key] for key in self.inputButtons.keys()]:
			keysPressed.append(allKeysPressed[act])

		inputs = []

		# vertical
		inputs.append(keysPressed[0]-keysPressed[1])
		# horizontal
		inputs.append(keysPressed[2]-keysPressed[3])

		if returning:
			return inputs
		elif len(self.totalInputs) < self.bg["currentFrame"]:
			self.totalInputs.append(inputs)



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

		image = pygame.surface.Surface((30, 50))
		image.fill("blue")
		offset = [0, 0]
		returnSprites.append([image, offset])

		return returnSprites



	def getCollision(self, inPos=None):

		if inPos == None:
			pos = self.pos
		else:
			pos = inPos

		return [
			[pos[0]-15, pos[1]+25],
			[pos[0]+15, pos[1]-25],
		]



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
			start[0] += (self.pos[0]-cam.pos[0]+pack[1][0])*scaling
			start[1] -= (self.pos[1]-cam.pos[1]+pack[1][1])*scaling
			rect = image.get_rect(center=start)

			scrn.blit(image, rect)
