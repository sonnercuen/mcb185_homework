# 34scoringmatrix.py by Conner Suen

nts = 'ACGT'
for nt in nts:
	if nt == 'A': print(' ', end='')
	print(' ', nt, end='')
print('')
for nt1 in nts:
	print(nt1, end = ' ')
	for nt2 in nts:
		if nt1 == nt2: print('+1', end = ' ')
		else:          print('-1', end = ' ')
	print()	

	