# 37nilakantha.py by Conner Suen

n = 2000
est = 3
for i in range(2, n+1, 2):
	den = 4 / (i * (i + 1) * (i + 2))
	if i % 4 == 0: est = est - den
	else: est = est + den
print(est)