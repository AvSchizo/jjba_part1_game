from JoJo_classes_part1.Base_Class import baseJoJoClass

class JoJoClass(baseJoJoClass):

	def __init__(self, globals, inputs=[]):
		super().__init__(globals, inputs)



	def update(self):
		self.doPhysics()



	def doPhysics(self):

		self.convertInputs()

		inputs = self.totalInputs[self.bg["currentFrame"]-1]

		acceleration = 1
		deceleration = [
			# 0: additive, 1: multiplicitive
			1,
			# additive deceleration
			4,
			# multiplicitive deceleration
			0.75,
			# multiplicitive deceleration threshold
			1,
		]
		maxSpeed = 10
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
				eeg = self.velocities["self"][i]
				# additive
				if deceleration[0] == 0:
					if abs(eeg) > deceleration[1]:
						self.velocities["self"][i] += (eeg/abs(eeg))*-1*deceleration[1]
					else:
						self.velocities["self"][i] = 0
				# multiplicitive
				elif deceleration[0] == 1:
					if abs(eeg) > deceleration[3]:
						self.velocities["self"][i] *= deceleration[2]
					else:
						self.velocities["self"][i] = 0

		# moving
		for key in self.velocities.keys():
			vel = self.velocities[key]
			for i in range(2):
				self.pos[i] += round(vel[i])
