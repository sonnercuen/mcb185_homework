# 24accuracy.py by Conner Suen

def accurate(TP, TN, FP, FN):
	if TP < 0 or TN < 0 or FP < 0 or FN < 0:
		return 'Cannot have negative cases.'
	else:
		acc = (TP + TN) / (TP + TN + FP + FN)
		f1 = TP / (TP + .5 * (FP + FN))
		return acc, f1 
test1 = accurate(50, 30, 5, 4)
test2 = accurate(-2, 80, 0, 2)
print(test1)
print(test2)