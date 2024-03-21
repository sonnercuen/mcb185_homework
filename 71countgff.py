# 71countgff.py by Conner Suen

import gzip
import sys

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		if feature not in count: count[feature] = 1
		else:                    count[feature] += 1
		if feature not in count: count[feature] = 0
		count[feature] += 1
	for f, n in count.items(): print(f, n)