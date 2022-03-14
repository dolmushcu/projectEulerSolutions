def check(element):
    e = element
    sayac = 1

    while e > 1:
        if e % 2 == 0:
            e = e // 2
            sayac += 1
        else:
            e = (3 * e) + 1
            sayac += 1
    
    return sayac

max = 0
number = 0

for i in range(3, 1000000):
    chain = check(i)
    if chain > max:
        max = chain
        number = i

print("Longest chain: " + str(max))
print("Number that produced the chain: "+ str(number))