# 44randompi.py by Conner Suen

import math
import random

hits = 0
shots = 0
est = 0
while True:
	x = random.random()
	y = random.random()
	r = math.sqrt((x ** 2) + (y ** 2))
	shots += 1
	if r < 1: 
		hits += 1
	print(4 * (hits / shots))
		