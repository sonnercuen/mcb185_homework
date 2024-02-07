# 33triples.py by Conner Suen

for i in range(1, 100):
	a = i
	for j in range(i + 1, 100):
		b = j
		c = (a ** 2 + b ** 2) ** (1/2)
		if   c % 1 == 0: print(a, b, c)	