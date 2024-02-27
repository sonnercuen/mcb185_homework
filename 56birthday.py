# 56birthday.py by Conner Suen

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
match = 0

for k in range(trials):
	birthdays = []
	for per in range(people):
		per = random.randint(0, days - 1)
		birthdays.append(per)
	shared = False
	for i in birthdays:
		for j in birthdays[i + 1:]:
			if i == j: 
				shared = True
	if shared == True: match += 1
print(match / trials)
