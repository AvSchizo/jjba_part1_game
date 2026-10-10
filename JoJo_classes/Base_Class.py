import pygame
pygame.init()

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