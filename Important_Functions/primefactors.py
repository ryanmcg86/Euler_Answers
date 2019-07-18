'''The function to get all the prime factors of a given input n'''

def factors(n):
    factors = []
    for i in range(2, 4):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n /= i
    for i in range(5, int(n**0.5) + 1, 6):
        plus2 = [i, i + 2]
        for j in plus2:
            if n % j == 0:
                factors.append(j)
                while n % j == 0:
                    n /= j
    if n > 2:
        factors.append(n)
    return factors
