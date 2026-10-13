def loadMapGeo(path):

	def textIntoPoints(text):
		nums = text.split(",")
		sec = []
		for num in nums:
			if len(num.split(".")) == 1:
				sec.append(int(num))
			elif num.split(".")[1] == "":
				sec.append(int(num.split(".")[0]))
			else:
				sec.append(float(num))
		return sec

	with open(path, "r") as f:
		content = f.read().splitlines()



	geoLines = []

	for line in content:

		lineData = {
			"points": [],
			"direction": None,
			"deadly": False,
		}

		data = line.split()

		if len(data) == 0:
			continue

		# points
		if data[1] == "\\|":
			lineData["points"] = [textIntoPoints(data[0]), textIntoPoints(data[0])]
		else:
			lineData["points"] = [textIntoPoints(data[0]), textIntoPoints(data[1])]

		## gets rid of points to be read
		for i in range(2):
			data.pop(0)


		# other data
		for thing in data:

			key, val = data.split("=")

			if val.lower() == "false" or val.lower() == "true":
				val = bool(val)


			lineData[key] = val


		geoLines.append(lineData)


	return geoLines