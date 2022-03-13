# tekrarli permutasyon
def factorial(n):
	m = 1
	for i in range(1, n+1):
		m *= i
	return m

def grid(x, y):
	return factorial(x+y)//(factorial(x)*factorial(y))

print(grid(20,20))