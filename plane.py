import random

class Plane(object):
	"""Class represents a plane object"""
	def __init__(self, angle):
		"""Constructor method"""
		self.angle = angle
	def adjust(self):
		"""Returns an angle adjustment"""
		return self.angle/2.0
	def std_error(self, a, b):
		"""Returns a standard error"""
		return random.gauss(a,b) 
	@property
	def angle(self):
		return self.__angle

	@angle.setter
	def angle(self, angle):
		self.__angle = angle
