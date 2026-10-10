class cameraClass():

	def __init__(self, startPos=[0, 0], inDist=0, scaleRef=[1/2, 10]):

		self.pos = startPos

		self.distance = inDist

		self.scalingRef = scaleRef



	def getScaling(self, objDist=0, specScaleRef=None):

		if specScaleRef == None:
			ref = self.scalingRef
		else:
			ref = specScaleRef

		return ref[0]**((1/ref[1])*(self.distance-objDist))