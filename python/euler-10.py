# sieve of eratosthenes

import math, time

startTime = time.time()

length = 2000000
numbers = [True] * (length+1)

numbers[0] = False
numbers[1] = False

i = 2
while i < length:
  if numbers[i]:
    for j in range(2, (length//i)+1):
      numbers[j*i] = False
  i += 1

primes = [k for k, v in enumerate(numbers) if v]
print(sum(primes), "execution time: " + str(time.time() - startTime) + "s", sep="\n")