'''This function returns the number of positive divisors of n'''
from math import prod

def tau(n):
    exps = []
    for i in range(2, 4):
        if n % i == 0: exps.append(0)
        while n % i == 0:
            exps[-1] += 1
            n /= i
    for i in range(5, int(n**0.5) + 1, 6):
        plus2 = [i, i + 2]
        for j in plus2:
            if n % j == 0: exps.append(0)
            while n % j == 0:
                exps[-1] += 1
                n /= j
    if n > 2: exps.append(1)
    return prod(i + 1 for i in exps)
