# 23hydropathy.py by Conner Suen

aa = 'amino acid'
def hydropathy(aa):
	if   aa == 'A':
		print(float(1.80))
	elif aa == 'C':
		print(float(2.50))
	elif aa == 'F': 
		print(float(2.80))
	elif aa == 'G':
		print(float(-0.40))
	elif aa == 'H':
		print(float(-3.20))
	elif aa == 'I':
		print(float(4.50))
	elif aa == 'K':
		print(float(-3.90))
	elif aa == 'L':
		print(float(3.80))
	elif aa == 'M':
		print(float(1.90))
	elif aa == 'Q':
		print(float(-3.50))
	elif aa == 'D':
		print(-3.50)
	elif aa == 'E':
		print(-3.50)
	elif aa == 'N':
		print(-3.50)
	elif aa == 'P':
		print(float(-1.60))
	elif aa == 'R':
		print(float(-4.50))
	elif aa == 'S': 
		print(-0.80)
	elif aa == 'T':
		print(-0.70)
	elif aa == 'V': 
		print(4.20)
	elif aa == 'W': 
		print(-0.90)
	elif aa == 'Y':
		print(-1.30)
	elif aa == 'B':
		print('Not an amino acid letter.')
		return aa 
noname = hydropathy('B')
ala = hydropathy('A')
gly = hydropathy('G')

	