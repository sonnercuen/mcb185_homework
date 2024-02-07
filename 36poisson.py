# 36poisson.py by Conner Suen

import math
def poisson(n, k):
	factk = 1
	for i in range(1, k + 1):
		factk = factk * i
	prob = ((n**k) * (math.e ** -n)) / factk
	return prob
print(poisson(1, 2))