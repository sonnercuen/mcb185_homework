# dogma.py by Conner Suen

import math
import sys
import mcb185

def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

# first translation function
'''
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i + 3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)
'''

# second translation function
def translate(dna):
	codons = ('ATG', 'TAA')
	aminos = 'M*'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i + 3]
		if codon in codons:
			'''
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
			'''
			aas.append(aminos[codons.index(codon)])
		else:
			aas.append('X')
	return ''.join(aas)
	
def gc_comp(seq):
	comp = seq.count('C') + seq.count('G')
	return (comp / len(seq))

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
#codons

def transcription(template):
	comp = []
	#mrna = []
	for i in range(len(template)):
		if template[i] == 'A': comp.append('U')
		elif template[i] == 'G': comp.append('C')
		elif template[i] == 'C': comp.append('G')
		elif template[i] == 'T': comp.append('A')
	mrna = ''.join(comp)
	return mrna
	
def translate(dna):
	codons = ('TTT', 'TTC', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG',
			  'ATT', 'ATC', 'ATA', 'ATG', 'GTT', 'GTC', 'GTA', 'GTG',
			  'TCT', 'TCC', 'TCA', 'TCG', 'CCT', 'CCC', 'CCA', 'CCG',
			  'ACT', 'ACC', 'ACA', 'ACG', 'GCT', 'GCC', 'GCA', 'GCG',
			  'TAT', 'TAC', 'TAA', 'TAG', 'CAT', 'CAC', 'CAA', 'CAG',
			  'AAT', 'AAC', 'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG',
			  'TGT', 'TGC', 'TGA', 'TGG', 'CGT', 'CGC', 'CGA', 'CGG',
			  'AGT', 'AGC', 'AGA', 'AGG', 'GGT', 'GGC', 'GGA', 'GGG')
	aminos = 'FFLLLLLLIIIMVVVVSSSSPPPPTTTTAAAAYY**HHQQNNKKDDEECC*WRRRRSSRRGGGG'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			# idx = codons.index(codon)
			# aa = aminos[idx]
			# aas.append(aa)
			aas.append(aminos[codons.index(codon)])
		else:
			aas.append('X')
	return ''.join(aas)

def meltemp(sequence):
	for nt in sequence:
		a = sequence.count('A')
		t = sequence.count('T')
		c = sequence.count('C')
		g = sequence.count('G')
	nt = a + t + c + g
	if nt <= 13:
		mp = (a + t) * 2 + (g + c) * 4
	if nt > 13:
		mp = 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
	return mp