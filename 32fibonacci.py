# 32fibonacci.py by Conner Suen

val1 = 0
val2 = 1
for i in range(5):
	print(val1)
	print(val2)
	val1 = val2 + val1
	val2 = val2 + val1
print()
