# 84splicesites.py by Conner Suen

import gzip
import sys
import mcb185

fasta = sys.argv[1]
gff = sys.argv[2]

def print_pwm(pwm, ac, id, de):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('XX')
	print('DE', de)
	print('PO	A	C 	G 	T')
	for i, d in enumerate(pwm):
		print(i + 1, end='\t')
		for nt, n in d.items():
			print(n, end='\t')
		print()
	print('//')

chrom = {}
for defline, seq in mcb185.read_fasta(fasta):
	chid = defline.split()[0]
	chrom[chid] = seq

introns = []
with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.split('\t')
		c = f[0]
		t = f[2]
		b = int(f[3]) - 1
		e = int(f[4]) - 1
		n = f[5]
		s = f[6]
		if t != 'intron': continue
		introns.append([c, b, e, n, s])
don = []
for i in range(6):
	don.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

acc = []
for i in range(8):
	acc.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

for c, b, e, n, s in introns:
	if s == '+':
		iseq = chrom[c][b: e + 1]
	else:
		iseq = mcb185.anti_seq(chrom[c][b: e + 1])
	
	dseq = iseq[0: 6]
	for i, nt in enumerate(dseq):
		don[i][nt] += n
	
	aseq = iseq[-8:]
	for i, nt in enumerate(aseq):
		acc[i][nt] += n

print_pwm(acc, 'ik001', 'ACC', 'splice acceptor')
print_pwm(don, 'ik002', 'DON', 'donor site')
	