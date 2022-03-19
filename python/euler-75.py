import math

L = 1500000
lengths = [0] * (L + 1)
for m in range(2, int(math.sqrt(L/2))):
  for n in range(1, m):
    if (m+n) % 2 == 1 and math.gcd(m, n) == 1:
      length = 2*(m*(m+n))
      for i in range(1, (L//length)+1):
        lengths[length * i] += 1

print(len(list(filter(lambda x: x == 1, lengths))))