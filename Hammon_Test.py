import pygame
pygame.init()


ham = {
	#
	## how much hammon you have
	"level": 0,
	"maxLevel": 3000,
	"progression": 10,
	"detention": -5,
	"natDrain": -1,
	## whether it's rising or lowering
	"progress": 0,
	"maxProgress": [
		# in
		180,
		# out
		120
	],
	"stillTime": 60,
	"cooldown": 120,
	### 1: up; 2: down;
	"stage": 1,
	#
}


font = pygame.font.Font(None, 40)




def safetyStats():

	if ham["level"] > ham["maxLevel"]:
		ham["level"] = ham["maxLevel"]

	if ham["level"] < 0:
		ham["level"] = 0












if __name__ != "__main__":
	quit()




screen = pygame.display.set_mode([400, 300])
clock = pygame.time.Clock()



while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			quit()



	# calcs
	if pygame.key.get_pressed()[pygame.K_SPACE]:
		pressing = True
	else:
		pressing = False


	if ham["cooldown"] > 0:
		ham["cooldown"] -= 1
		ham["level"] += ham["natDrain"]

	else:

		if ham["stage"] == 1:
			if ham["progress"] >= ham["maxProgress"][0]:
				ham["cooldown"] = ham["stillTime"]
				ham["progress"] = 0
				ham["stage"] = 2
			else:
				if pressing:
					ham["level"] += ham["progression"]
				else:
					ham["level"] += ham["detention"]
				ham["progress"] += 1

		elif ham["stage"] == 2:
			if ham["progress"] >= ham["maxProgress"][1]:
				ham["cooldown"] = ham["stillTime"]
				ham["progress"] = 0
				ham["stage"] = 1
			else:
				if pressing:
					ham["level"] += ham["detention"]
				ham["level"] += ham["natDrain"]
				ham["progress"] += 1

	safetyStats()




	if ham["cooldown"] > 0:
		updownText = "still"
	elif ham["stage"] == 1:
		updownText = "up"
	else:
		updownText = "down"
	ham["text"] = {
		"updown": font.render("direction: " + updownText, True, "black"),
		"cooldown": font.render("cooldown: " + str(ham["cooldown"]), True, "black"),
		"level": font.render("level: " + str(round(ham["level"]/ham["maxLevel"]*100)) + "%", True, "black"),
		"progress": font.render("progress: " + str(round(ham["progress"]/ham["maxProgress"][ham["stage"]-1]*100)) + "%", True, "black"),
	}








	# drawing
	screen.fill("lavender")
	prog = 0
	for text in [ham["text"][key] for key in ham["text"].keys()]:
		screen.blit(text, [0, prog])
		prog += text.get_rect().height


	pygame.display.update()



	clock.tick(60)