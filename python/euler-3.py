# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math, copy

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

def max_prime_factor(number):
	number_copy = copy.deepcopy(number)
	prime_factors_arr = []
	count = 3

	if is_prime(number):
		prime_factors_arr.append(number)
	else:
		while number_copy%2 == 0:
			number_copy = number_copy//2
			prime_factors_arr.append(2)

		while number_copy > 1:
			if not is_prime(count):
				count+=2
				continue
			else:
				while number_copy%count == 0:
					number_copy = number_copy//count
					prime_factors_arr.append(count)
					if is_prime(number_copy):
						prime_factors_arr.append(number_copy)
						number_copy = number_copy//number_copy
				count+=2

	return max(prime_factors_arr)

print(max_prime_factor(600851475143))