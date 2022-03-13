arr = [(3,5,7,9)]
a = 4
b = 4

for i in range(499):
	f = arr[i][3] + b
	arr.append((f,f+a,f+a*2,f+a*3))
	b += 2
	a += 2

s = 1
for i in arr:
	s += i[0]+i[1]+i[2]+i[3]

print(s)
