# 62skewer.py by Conner Suen

import dogma
import sys
import gzip

w = int(sys.argv[2])
seq = sys.argv[1]

#seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
		
g = seq[0:w].count('G')
c = seq[0:w].count('C')

for i in range(len(seq) - w):
	s = seq[i:i + w]
	new = seq[i + w]
	dump = seq[i]
	if i == 0:
		if g + c != 0:
			print(i, (g + c) / len(s), (g - c) / (g + c))
		else:
			print(i, (g + c) / len(s), 0)

	if dump == 'C': c -= 1
	elif dump == 'G': g -= 1
	
	if new == 'C': c += 1
	elif new == 'G': g += 1
	
	if g + c == 0: comp = 0
	else:
		comp = (g + c) / len(s)
		skew = (g - c) / (g + c)
	print(i + 1, comp, skew)





'''
for i in range(len(seq) - w + 1): # 17
	s = seq[i:i + w]
	if i == 0:
	else:
		if seq[i - 1] == 'G': g -= 1
		elif seq[i - 1] == 'C': c -= 1
		elif s[w - 1] == 'G': g += 1
		elif s[w - 1] == 'C': c += 1
		print(i, (g + c) / len(s))
		print(g, s, s[w - 1])
'''
	
	