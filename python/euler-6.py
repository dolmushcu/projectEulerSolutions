# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# https://en.wikipedia.org/wiki/Square_number
# 1^2+2^2+3^2+...+n^2 => (n(n+1)(2n+1))/6
#
# 1+2+3+...+n => (n(n + 1))/2

n = 100
sum_of_squares = (n*(n + 1)*(2*n + 1))//6
square_of_the_sum = ((n*(n + 1))//2)**2

print(square_of_the_sum - sum_of_squares)