from JoJo_classes.Base_Class import baseJoJoClass

class JoJoClass(baseJoJoClass):

	def __init__(self, globals, inputs=[]):
		super().__init__(globals, inputs)



	def update(self):
		self.doPhysics()



	def doPhysics(self):

		self.convertInputs()

		inputs = self.totalInputs[self.bg["currentFrame"]-1]

		speed = 5
		self.velocities["self"][0] = inputs[0]*speed
		self.velocities["self"][1] = inputs[1]*speed

		# moving
		for key in self.velocities.keys():
			vel = self.velocities[key]
			for i in range(2):
				self.pos[i] += vel[i]