# 45dndstats.py by Conner Suen

import random

# 3D6
rolls = 1000
stat1 = 0
avg = 0
for i in range(1, rolls + 1):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	stat1 = (d1 + d2 + d3) 
	avg = avg + stat1
print(avg / rolls)

# 3D6r1
trials = 1000
overall = 0
for j in range(1, trials + 1):
	stat2 = 0
	for i in range(1, 4):
		d = random.randint(1, 6)
		if d == 1:
			d = random.randint(1, 6)
		stat2 = stat2 + d
	overall = overall + stat2
print(overall / trials)

# 3D6x2
throws = 1000
stat3 = 0
maxavg = 0
for i in range(1, throws + 1):
	stat3 = 0
	for j in range(1, 4):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2: stat3 += d1
		else: stat3 += d2
	maxavg += stat3
print(maxavg / throws)

# 4D6d1
droll = 1000
stat4 = 0
favg = 0
for i in range(1, droll + 1):
	stat4 = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if   d1 <= d2 and d1 <= d3 and d1 <= d4: stat4 = d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: stat4 = d1 + d3 + d4
	elif d3 <= d1 and d3 <= d2 and d3 <= d4: stat4 = d1 + d2 + d4
	else: stat4 = d1 + d2 + d3
	favg += stat4
print(favg / droll)