# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def is_prime(number):
	if number == 2:
		return True
	elif number < 2 or number%2 == 0:
		return False
	else:
		for a in range(2,math.ceil(math.sqrt(number))+1):
			if number % a == 0:
				return False
		return True

number = 3
count = 1

while True:
	if is_prime(number):
		count+=1
		if count == 10001:
			print(number)
			break
	number+=2