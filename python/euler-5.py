# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import copy

# least common multiple
def lcm(arr):
	arr_c = copy.deepcopy(arr)
	divisors_arr = []
	divisor = 2

	while [1]*len(arr) != arr_c:
		check = [True for i in arr_c if i%divisor==0]
		
		while True in check:
			for index, key in enumerate(arr_c):
				arr_c[index] = key // divisor if key % divisor == 0 else arr_c[index]

			check = [True for i in arr_c if i%divisor==0]
			divisors_arr.append(divisor)

		divisor+=1


	result = 1
	for i in divisors_arr:
		result *= i
	return result


print(lcm(list(range(1,21))))