# co-author by Vanessa Su and Conner Suen

import random

roll = 10000

# DC 
for j in [5, 10, 15]:
	dsuc = 0
	dfail = 0
	for i in range(roll):
		d = random.randint(1, 20)
		if d >= j: dsuc += 1
		else:      dfail += 1
	print(f'DC {j}', (dsuc / roll), sep='\t')

# DC advantage
for j in [5, 10, 15]:
	dasuc = 0
	dafail = 0
	for i in range(roll):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 >= d2:
			if d1 >= j: dasuc += 1
			else:       dafail += 1
		else:
			if d2 >= j: dasuc += 1
			else:       dafail += 1
	print(f'DCa {j}', (dasuc / roll), sep='\t')

# DC disadvantage
for j in [5, 10, 15]:
	ddsuc = 0
	ddfail = 0
	for i in range(roll):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 <= d2:
			if d1 >= j: ddsuc += 1
			else:       ddfail += 1
		else:
			if d2 >= j: ddsuc += 1
			else:       ddfail += 1
	print(f'DCd {j}', (ddsuc / roll), sep='\t')
