import pygame
pygame.init()
clock = pygame.time.Clock()


###################
#   preferences   #
###################
import json
from verifyPreferences import verifyPreferences
from savePreferences import savePreferences

# default preferences here
defaultPreferences = {
	"screenSizeScale": 1,
	"webMode": False,
	"maxFPS": 75,
	"collisionDrawing": {
		"active": True,
		"floorColor": "red",
	},
}

verifyPreferences(defaultPreferences)

with open("preferences.json", "r") as f:
	preferences = json.load(f)




###################
#     globals     #
###################
gs = {
	"running": True,
	"currentFrame": 0,
	# if gameSate%100 == 0, that is a loading state, and will trigger the load function for whatever the hundreds place is
	# so please change it to 100 for release
	"gameState": 200,
	"substate": 0,
	"tickRate": 60,
	"FPS": 75,
	# you can get positions bigger than these, this just gives a reference for how to scale things
	"spacetimeSize": [1600, 900],
}

screen = pygame.display.set_mode((preferences["screenSizeScale"]*gs["spacetimeSize"][0], preferences["screenSizeScale"]*gs["spacetimeSize"][1]))




#
# load JoJos
#
from JoJoClassesImport import bigList as jojoList





def load_movementTest():
	pass





def mainLoop():

	gs["currentFrame"] += 1


	if gs["gameState"] == 200:
		pass






def renderAll():

	# sum sum



	pygame.display.update()






if __name__ != "__main__":
	quit()

while gs["running"]:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			quit()