import json
import sys
import itertools
'''
person = {
	'name': 'Ian Korf',
	'age': '57',
	'weight': '163.8',
	'pets': ['Hesper', 'Mouserat', 'Labrat'],
	'mentees': {
		'Claire': 'undergrad',
		'Dell': 'undergrad',
	}
}

print(json.dumps(person, indent = 4))

print(person['mentees']['Claire'])
people = []
people[0]['made this up'] = 'hello'
people[0]['mentees']['Ismael'] = 'grad'
people[0].append('Hesper', 'Fizzbuzz', 'Mouserat')

k = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i + k]
		if kmer not in kloc: kloc[kmer] = {}
		if chrom not in kloc[kmer]: kloc[kmer][chrom] = []
		klock[kmer][chrom].append(i)
print(json.dumps(kloc, indent=4))

83
kno what transfac looks like
'''
d = {'dog': 'woof', 'cat': 'meow'}
print(d['cat'])
d['pig'] = 'oink'
print(d)
for key in d: print(f'{key} says {d[key]}')
# or
for k, v in d.items(): print(k, 'says', v)

for nts in itertools.product('ACGT', repeat = 2):
	print(nts)