s = 0
for i in range(10**6+1):
	if str(i) == str(i)[::-1] and "{0:b}".format(i) == "{0:b}".format(i)[::-1]:
		s += i
print(s)