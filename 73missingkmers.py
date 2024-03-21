# 73missingkmers.py by Conner Suen
import sys
import itertools
import mcb185

def seq_dict(seq, k):
	kcount = {}
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i + k]
		if kmer not in kcount: kcount[kmer] = 1
	return kcount

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	rev = mcb185.anti_seq(seq)
	k = 0
	found = 0
	kmercount = 0
	while True:
		k += 1
		kcount = seq_dict(seq, k)
		kcount2 = seq_dict(rev, k)
		for kmer in kcount2:
			kcount[kmer] = 1
		for nts in itertools.product('ACGT', repeat = k):
			kmer = ''.join(nts)
			if kmer in kcount: continue
			else:
				kmercount += 1
				print(kmer, kmercount)
				found += 1
		if found != 0: break

		
