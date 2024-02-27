# 52genomestats.py by Conner Suen


'''
gffpath = sys.argv[1]
feature = sys.argv[2]

with gzip.open(gffpath, 'rt') as fp:
	length = size.split()
max = length[5]
min = length[5]
for i in range(len(sys.argv[2])):
	if max < length[i]:
		max = length[i]
	else: continue
	if min > length[i]:
		min = length[i]
	else: continue
print([min, max])

# prints list added in terminal
# go from 1 input to end in terminal - get rid of prog name
print(sys.argv[1:])

val = []
for x in features:
	print(x)
	val.append(int(x))
val.sort()
print(val)


'''

import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]
max = 0
length = []
with gzip.open(gffpath, 'rt') as fp:
	for j in fp:
		row = j.split()
		if row[2] == feature:
			start = int(row[3])
			stop = int(row[4])
			length.append(stop - start + 1)
		else: continue
		length.sort()
		min = length[0]
		genome = 0
		std = 0
		for i in length:
			genome += i
			if max < i:
				max = i
			else: continue
			if min > i:
				min = i
			else: continue
		mean = int(genome) / len(length)
		if len(length) % 2 != 0:
			med = length[len(length) // 2]
		else:
			med = (length[(len(length) - 1) // 2] + length[((len(length) - 1) // 2) + 1]) / 2
		for spec in length:
			std += (spec - mean) ** 2
		dev = math.sqrt(std / len(length))
	
	print(len(length))
	print(min)
	print(max)
	print(round(mean))
	print(round(dev))
	print(round(med))
	

