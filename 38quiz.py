#Quiz by Conner Suen and Ahbi Sharma

denom = 1
pi = 1
sign = 1
def estimate(n):
	for i in range(1,n):
		denom = i*2 + 1
		x = pi - (1 / denom) 
		sign = i * -1 
		x*4
	return x
answer = estimate(100)
print(answer)
	
		
	