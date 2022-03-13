from math import sqrt
from itertools import count, islice

def primesSum(n):
	arr = [True]*(n+1)
	arr[0] = False
	arr[1] = False

	primes = []

	for i in range(2, int(n**.5)+1):
		if arr[i]:
			for j in range(i**2, n+1, i):
				if j > n: break
				arr[j] = False

	for index, value in enumerate(arr):
		if value:
			primes.append(index)

	sums = [primes[0]]
	for i in range(1, len(primes)):
		sums.append(sums[i-1]+primes[i])

	return sums

sums = primesSum(10**6)

def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

m = 0
r = 0
for i in sums[::-1]:
	if i < 1001700:
		r = i
		break

print(r)