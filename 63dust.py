# 63dust.py by Conner Suen

import sys
import mcb185
import math

def entropy(a, t, g, c):
	tot = a + t + g + c
	pa = a / tot 
	pt = t / tot
	gt = g / tot
	ct = c / tot
	if pa == 0: aterm = 0
	else: aterm = -pa * math.log2(pa)
	if pt == 0: tterm = 0
	else: tterm = -pt * math.log2(pt)
	if gt == 0: gterm = 0
	else: gterm = -gt * math.log2(gt)
	if ct == 0: cterm = 0
	else:cterm = -ct * math.log2(ct)
	H = aterm + tterm + gterm + cterm
	return H

results = []
names = []
w = int(sys.argv[2])
for defline, sequence in mcb185.read_fasta(sys.argv[1]):
	genome = list(sequence)
	names.append(defline)
	for i in range(len(sequence) - w + 1):
		s = sequence[i: i + w]
		a = s.count('A')
		g = s.count('G')
		c = s.count('C')
		t = s.count('T')
		H = entropy(a, t, g, c)
		if H < float(sys.argv[3]):
			for n in range(i, i + w):
				genome[n] = 'N'
	results.append(''.join(genome))
for name, result in zip(names, results):
	print(f'>{name}')
	for i in range(0, len(result), 60):
		print(result[i: i + 60])