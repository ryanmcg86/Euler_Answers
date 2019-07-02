def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def build_sieve(n):
    if n < 2:
        return []
    if n < 3:
        return [2]
    prime_sieve = [2, 3]
    i = 5
    while i <= n:
        if isPrime(i):
            prime_sieve.append(i)
        if i + 2 > n:
            break
        if isPrime(i + 2):
            prime_sieve.append(i + 2)
        i += 6
    return prime_sieve

def solve(n):
    start = time.time()
    primes = build_sieve(n)
    ans = 0
	
    for prime in primes:
        string_prime = str(prime)
        for n in range(0, len(string_prime)):
            count = 0
            for i in '0123456789':
                permutation = int(string_prime.replace(string_prime[n], i))
                if isPrime(permutation):
                    if permutation >= prime:
                        count += 1
            if count == 8:
                ans = string_prime
                break
        if ans != 0:
            break

    print ans
    print str(time.time() - start)
