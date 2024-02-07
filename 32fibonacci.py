# 32fibonacci.py by Conner Suen
def fibonacci(n):
	val1 = 0
	val2 = 1
	end = ' '
	for i in range(n):
		print(val1)
		print(val2)
		val1 = val2 + val1
		val2 = val2 + val1
	return end 
print(fibonacci(5))