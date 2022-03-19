# When m and n are any two positive integers(m > n):
#
#     a = 2mn
#     b = m^2 − n^2
#     c = m^2 + n^2
#
# Then a, b and c form a Pythagorean Triple. This is known as "Euclid's formula".
# To find only the pirimitive triples m and n must be coprimes and one must be odd while other is even
# After we find the pirimitive ones we can just multiple them with a constant and get all of the triples.
#
#     a = k(2mn)
#     b = k(m^2 − n^2)
#     c = k(m^2 + n^2)

import math

L = 1000
for m in range(2, int(math.sqrt(L/2))):
  for n in range(1, m):
    if (m+n) % 2 == 1 and math.gcd(m, n) == 1:
      length = 2*(m*(m+n))
      if L % length == 0:
        k = L // length
        a = k*(2*m*n)
        b = k*(m*m-n*n)
        c = k*(m*m+n*n)
        print(a*b*c)