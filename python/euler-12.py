def divisorNum(e):
  count = 2
  max = e

  i = 2
  while i < max:
    if e % i == 0:
      count += 2
      max = e // i
    i += 1
  
  return count

sum = 0
for i in range(10000000):
  sum += i
  if divisorNum(sum) > 500:
    print(sum)
    break