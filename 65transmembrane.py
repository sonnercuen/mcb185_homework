# 65transmembrane.py by Conner Suen

import dogma
import sys
import mcb185

names = []
genome = []
defcount = 0
#hydropathy scores
def hydropathy(protein):
	hp = 0
	for aa in protein:
		if aa == 'I': hp += 4.5
		if aa == 'V': hp += 4.2
		if aa == 'L': hp += 3.8
		if aa == 'F': hp += 2.8
		if aa == 'C': hp += 2.5
		if aa == 'M': hp += 1.9
		if aa == 'A': hp += 1.8
		if aa == 'G': hp += -0.4
		if aa == 'T': hp += -0.7
		if aa == 'S': hp += -0.8
		if aa == 'W': hp += -0.9
		if aa == 'Y': hp += -1.3
		if aa == 'P': hp += -1.6
		if aa == 'H': hp += -3.2
		if aa == 'E': hp += -3.5
		if aa == 'Q': hp += -3.5
		if aa == 'D': hp += -3.5
		if aa == 'N': hp += -3.5
		if aa == 'K': hp += -3.9
		if aa == 'R': hp += -4.5
	return hp
	
for defline, protein in mcb185.read_fasta(sys.argv[1]):
	names.append(defline)
	verify = False
	verify2 = False
	for i in range(23):
		s = protein[i:i + 8]
		hp = hydropathy(s)
		if hp / 8 >= 2.5 and s.find('P') == -1:
			verify = True
			break
		
	for k in range(30, len(protein) - 10):
		w = protein[k:k + 11]
		thp = hydropathy(w)
		if thp / 11 >= 2.0 and w.find('P') == -1:
			verify2 = True
			break

	if verify and verify2:
		defcount += 1
		for i in range(0, len(defline), 1000):
			print(defline[i:i + 60], defcount)

	
		