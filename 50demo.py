# 50demo.py by Conner Suen

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])
for i in range(len(seq)):
	print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
for i, nt in enumerate(nts):
	print(i, nt)
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i + 1, nt, name)

nts = ['A', 'T', 'C']
nts[2] = 'G'
print(nts)
last = nts.pop()
print(last)
nts.sort()
print(nts)
nts.sort(reverse = True)
print(nts)
text = 'good day	to you'
words = text.split()
print(words)

# maximum
def ends(nums):
	numin = nums[0]
	numax = nums[0]
	for i in nums:
		if i < numin: numin = i
		if i > numax: numax = i
	return numin, numax