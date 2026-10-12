from JoJo_classes_part1.Base_Class import baseJoJoClass

class JoJoClass(baseJoJoClass):

	def __init__(self, globals, inputs=[]):
		super().__init__(globals, inputs)



	def update(self):
		self.doPhysics()



	def doPhysics(self):

		self.convertInputs()

		inputs = self.totalInputs[self.bg["currentFrame"]-1]

		acceleration = 5
		deceleration = 10
		maxSpeed = 30
		for i in range(2):
			# acceleration
			if inputs[i] != 0:
				dist = inputs[i]*maxSpeed-self.velocities["self"][i]
				if abs(dist) < acceleration:
					self.velocities["self"][i] += inputs[i]*acceleration
				# if on same side of zero
				elif dist*inputs[i] > 0:
					self.velocities["self"][i] += dist
			# deceleration
			else:
				if abs(self.velocities["self"][i]) > deceleration:
					self.velocities["self"][i] += inputs[i]*deceleration
				else:
					self.velocities["self"][i] = 0

		# moving
		for key in self.velocities.keys():
			vel = self.velocities[key]
			for i in range(2):
				self.pos[i] += vel[i]
