# 25entropy.py by Conner Suen

import math
def entropy(a, t, g, c):
	tot = a + t + g + c 
	pa = a / tot 
	pt = t / tot
	gt = g / tot
	ct = c / tot
	if   a == 0 or t == 0 or g == 0 or c == 0:
		return('Cannot have 0 of one nucleotide type')
	else:
		H = -pa * math.log2(pa) - pt * math.log2(pt) - gt * math.log2(gt) - \
			ct * math.log2(ct)
		return H
tst1 = entropy(25, 25, 30, 30)
print(tst1)
tst2 = entropy(0, 25, 30, 30)
print(tst2)
	