# 80demo.py by Conner Suen
import json
import dogma
'''
d = [
	'hello',
	(3.14, pi),
	[-1, 0, 1],
	{'year': 2000, 'month': 10}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])

def read_catalog(filepath):
	catalog = []
	with open(filepath)as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name: name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog
	
catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])

for primer in catalog:
	primer['Tm'] = dogma.meltemp(primer['Sequence'])
print(catalog)


seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 3
kloc = {}
for i in range(len(seq) - k + 1):
	kmer = seq[i:i + k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)
'''
truc = {
	'animals': {'dog': 'woof', 'cat': 'meow',  'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is_complete': False,
}
print(json.dumps(truc, indent = 4))