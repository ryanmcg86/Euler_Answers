'''This function returns a list of all of the proper divisors of a given input n'''

def properDivisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return list(sorted(set(divisors)))
