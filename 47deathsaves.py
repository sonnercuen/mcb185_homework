# 47deathsaves.py by Conner Suen

import random

success = 0
failure = 0
d = 0
s = 0
r = 0
n = 0
death = 0
live = 0
res = 0
roll = 1000
for i in range(roll):
	while True:
		d20 = random.randint(1, 20)
		n += 1
		if   d20 == 1: 
			failure += 2
			d += 2
		elif d20 == 20: 
			success = 3
			r += 1
			res += 1
			break
		elif d20 < 10: 
			failure += 1
			d += 1
		elif d20 >= 10: 
			success += 1
			s += 1
		if success == 3: 
			live += 1
			break
		if failure == 3: 
			death += 1
			break
print('P of death:', death / roll)
print('P of stabilizing:', live / roll)
print('P of revival:', res / roll) 
	
	