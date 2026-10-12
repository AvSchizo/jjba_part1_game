import pygame
pygame.init()


class guardClass():

	def __init__(self, keys):
		
		self.load()

		self.assignedKeys = keys
		self.beingPressed = False
	


	def reload(self, reloadTime=60):
		self.loaded = 0
		self.inReload = reloadTime
	


	def update(self, bullets=None):
		
		if self.inReload > 0:
			self.inReload -= 1
			if self.inReload == 0:
				if bullets != None:
					self.load(bullets)
				else:
					self.load()
		
		self.update()
	


	def load(self, bullets=5):
		self.loaded = bullets
		self.inReload = 0
	


	def checkPressed(self, inKeys=None):

		if inKeys == None:
			keys = self.assignedKeys
		else:
			keys = inKeys
		
		self.beingPressed = False
		akp = pygame.key.get_pressed()
		for key in keys:
			try:
				if akp[key]:
					self.beingPressed = True
					break
			except:
				pass




shD = {
	"inputList": [],
	"currentFrame": 0,
	"guards": [],
}




def addPressed(guards):

	l = []

	keys = pygame.key.get_pressed()

	for i in range(len())
	if keys[guardRuns[i]]:
		l.append(1)
	else:
		l.append(0)
	
	return l






if __name__ != "__main__":
	quit()



guardRuns = [
	pygame.K_1,
	pygame.K_2,
	pygame.K_3,
	pygame.K_4,
	pygame.K_5,
]
for i in range(5):
	shD["guards"].append(guardClass(keys=[guardRuns[i]]))



gl_shD = {
	"screen": pygame.display.set_mode((1600, 900)),
	"clock": pygame.time.Clock(),
}



while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			quit()
	

	# calcs
	while len(shD["inputList"]) < shD["currentFrame"]:
		shD["inputList"].append(addPressed(shD["guards"]))
	
	ins = shD["inputList"][shD["currentFrame"]-1]

	for i in range(len(shD["guards"])):

		g = shD["guards"][i]

		if g.loaded