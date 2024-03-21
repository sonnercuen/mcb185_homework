# 64profinder.py by Conner Suen and Henry Li

import dogma
import sys
import mcb185


for defline, sequence in mcb185.read_fasta(sys.argv[1]):
	proteins = []
	pros = []
	procount = 0
	#mrna = dogma.transcription(sequence)
	rdna = mcb185.anti_seq(sequence)
	#mrna2 = dogma.transcription(rdna)
	for i in range(3):
		aas = []
		proteins = dogma.translate(sequence[i:])
		proteins2 = dogma.translate(rdna[i:])
		aas.append(proteins)
		aas.append(proteins2)
		for aa in range(len(aas)):
			pros = aas[aa].split('*')
			for k in range(len(pros)):
				pro = pros[k] #[asdksdkMalksdjflaj*]
				if 'M' in pro:
					mindx = pro.find('M')
					profound = pro[mindx:]
					if len(profound) >= int(sys.argv[2]):
						procount += 1
						print(f'>NC_000913.3-prot-{procount}')
						print(profound + '*')
