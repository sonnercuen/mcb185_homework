# 21quadratic.py by Conner Suen

import math
def quadratic(a, b, c):
	inside = b**2 - 4 * a * c
	if   inside >= 0:
		x = float((-b - math.sqrt(inside))/(2 * a))
		y = float((-b + math.sqrt(inside))/(2 * a))
		return x, y
	if inside < 0: 
		return 'Cannot find square root of negative number.'
ans = quadratic(3, -5.86, 2.5408)
print(ans)
ans2 = quadratic(100, -5, 2.7)
print(ans2)