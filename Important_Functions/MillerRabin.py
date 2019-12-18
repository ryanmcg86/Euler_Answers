'''The following code finds whether big numbers are prime or not efficiently'''

def isPrime_dumb(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
#Build a Sieve of Eratosthenes
def SoE(n): 
    prime = [False] * 2 + [True for i in range(n - 1)]
    ans, p = [], 2
    while p**2 <= n: 
        if prime[p]: 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    return [i for i in range(n) if prime[i]]
    
def try_comp(a, d, n, s):
	if pow(a, d, n) == 1: return False
	for i in range(s):
		if pow(a, 2**i * d, n) == n - 1: return False
	return True
  
def MillerRabin(n, prec):
    d, s = n - 1, 0
    ps = SoE(prec)
    maxes = [1373653, 25326001, 118670087467, 2152302898747, 3474749660383, 341550071728321]
    while not d % 2:
        d, s = d >> 1, s + 1
    for i in range(len(maxes)):
        x = i + 2
        if n < maxes[i]:
            if i == 2 and n == 3215031751: return False
            return not any(try_comp(a, d, n, s) for a in ps[:x])
    return not any(try_comp(a, d, n, s) for a in ps)

def isPrime(n):
	if n < 10000:
		return isPrime_dumb(n)
	else:
		return MillerRabin(n, 25)
