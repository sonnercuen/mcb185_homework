# 82transfac.py by Conner Suen and Jonathan Raigosa

import json
import re
import sys
import gzip

matrices = []
with gzip.open(sys.argv[1], 'rt') as fp:
	record = ''
	for line in fp:
		if line.split()[0] == 'ID':
			info = line.split()[1]
			record = {
				'id': info,
				'pwm': []
			}
			matrices.append(record)
		elif re.search('[0123456789]', line.split()[0]):
			n, a, c, g, t = line.split()
			a = float(a)
			c = float(c)
			g = float(g)
			t = float(t)
			counts = {'A': a, 'C': c, 'G': g, 'T': t,}
			record['pwm'].append(counts)
print(json.dumps(matrices, indent=4))