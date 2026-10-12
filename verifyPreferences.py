import json

def verifyPreferences(default):

	blankDict = {}

	for key in default.keys():
		blankDict[key] = default[key]

	try:
		with open("preferences.json", "r") as f:
			prefDict = json.load(f)
	except FileNotFoundError:
		prefDict = {}

	for key in prefDict.keys():
		blankDict[key] = prefDict[key]


	with open("preferences.json", "w") as f:
		json.dump(blankDict, f, indent="\t")
