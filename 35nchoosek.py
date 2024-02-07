def factorial(n):
	fact = 1
	for i in range(1,n+1): 
		fact = fact * i 
	return fact
def nchoosek(n, k):
	prob = factorial(n) / (factorial(k) * factorial(n - k))
	return prob
print(nchoosek(4, 3))