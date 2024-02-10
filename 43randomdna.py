# 43randomdna.py by Conner Suen

import random


seqs = 4
for j in range(1, seqs):
	print(f'>seq-{j}')
	for i in range(1, random.randint(20, 30)):
		print(random.choice('ACGT'), end='')
	print()
	