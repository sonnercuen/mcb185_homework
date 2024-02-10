# 47deathsaves.py by Conner Suen

import random

death = 0
live = 0
res = 0
roll = 1000
for i in range(roll):
	success = 0
	failure = 0
	while True:
		d20 = random.randint(1, 20)
		if   d20 == 1: 
			failure += 2
		elif d20 == 20: 
			res += 1
			break
		elif d20 < 10: 
			failure += 1
		elif d20 >= 10: 
			success += 1
		if success == 3: 
			live += 1
			break
		if failure == 3: 
			death += 1
			break
print('P of death:', death / roll)
print('P of stabilizing:', live / roll)
print('P of revival:', res / roll) 
	
	