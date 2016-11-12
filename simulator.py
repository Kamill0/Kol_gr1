import random
import time
from plane import Plane


class Simulator(object):
	"""Class represents a simple flight simulator"""
	def __init__(self, angle):
		"""Constructor method"""
		self.plane = Plane(angle)

	def start(self): 
		"""Performs a simulation"""
		while True:
			self.plane.angle = self.plane.angle - self.plane.adjust() + self.plane.std_error(0,1)		
			print("Current angle: " + str(self.plane.angle))
			print("Applied correction: " + str(self.plane.adjust()))
			time.sleep(1)

if __name__ == "__main__":
	sim = Simulator(0)
	sim.start()
