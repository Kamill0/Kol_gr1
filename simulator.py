import random
import time

class Simulator(object):
	"""Class represents a simple flight simulator"""
	def __init__(self, angle):
		"""Constructor method"""
		self.angle = angle
	def adjust(self):
		"""Returns an angle adjustment"""
		return self.angle/2.0
	def std_error(self, a, b):
		"""Returns a standard error"""
		return random.gauss(a,b) 
	def start(self): 
		"""Performs a simulation"""
		while True:
			self.angle = self.angle - self.adjust() + self.std_error(0,1)		
			print("Current angle: " + str(self.angle))
			print("Applied correction: " + str(self.adjust()))
			time.sleep(1)

