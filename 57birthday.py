# 57birthday.py by Conner Suen

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
matches = 0

for j in range(trials):
	cal = []
	for i in range(days): cal.append(0)
	for i in range(people):
		pos = random.randint(0, days - 1)
		cal[pos] += 1
	for day in cal:
		if day > 1:
			matches += 1
			break
print(matches / trials)