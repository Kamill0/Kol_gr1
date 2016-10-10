#!/usr/bin/python
import random
import time


class Simulator:
	"Simulator"
	def __init__(self, angle):
		self.angle = angle
	def adj(self):
		return self.angle/2.0
	def stder(self, a, b):
		return random.gauss(a,b) 
	def start(self): 
		while True:
			self.angle = self.angle - self.adj() + self.stder(0,1)		
			
			print("Current angle: " + str(self.angle))
			print("Applied correction: " + str(self.adj()))
			time.sleep(1)

sim = Simulator(0)
sim.start()

