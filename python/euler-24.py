def factorial(n):
	m = 1
	for i in range(1, n+1):
		m *= i
	return m

def nthLexicographic(arr, wantedOrder):
	n = len(arr)
	result = []
	currentOrder = 0
	for i in range(1, n+1):
		x = 0
		while factorial(n - i) * (x+1) + currentOrder < wantedOrder and x < n - i:
			x += 1
		currentOrder += factorial(n - i) * x
		result.append(arr[x])
		arr.pop(x)

	return result

print(nthLexicographic([0,1,2,3,4,5,6,7,8,9], 1000000))