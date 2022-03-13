# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

#solution-1
def solution1(limit):
	arr = []

	for i in range(1, limit):
		if i*3 < limit:
			arr.append(i*3)
			if i*5 < limit:
				arr.append(i*5)
		else:
			break

	return sum(list(set(arr)))

#solution-2
def solution2(number):
	return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

#solution-3
def solution3(number):
    max3,max5,max15 = 0,0,0

    for i in range(number-1,0,-1):
        if i%3 == 0 and i//3 > max3:
            max3 = i//3

        if i%5 == 0 and i//5 > max5:
            max5 = i//5

        if i%15 == 0 and i//15 > max15:
            max15 = i//15

        if max3 != 0 and max5 != 0 and max15 != 0:
            break

    three = ((max3*(max3+1))//2)*3 # 3*(1+2+3+....+33)
    five = ((max5*(max5+1))//2)*5
    fifteen = ((max15*(max15+1))//2)*15

    return three + five - fifteen

print(solution1(1000))
print(solution2(1000))
print(solution3(1000))