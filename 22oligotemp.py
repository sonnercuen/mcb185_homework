# 22oligotemp.py by Conner Suen

def meltemp(a, t, c, g):
	nt = a + t + c + g
	if nt <= 13:
		mp = (a + t) * 2 + (g + c) * 4
	if nt > 13:
		mp = 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
	return mp	
short_tm = meltemp(2, 2, 3, 3)
long_tm = meltemp(10, 10, 13, 13)
med_tm = meltemp(5, 5, 10, 10)
print(short_tm)
print(med_tm)
print(long_tm)
