'''This funtion builds a prime sieve up to an input n, 
utilizing the isPrime function in the Important_Functions folder'''

def build_sieve(n):
    if n < 2: return []
    if n < 3: return [2]
    ps = [2, 3]
    i = 5
    while i <= n:
        if isPrime(i): ps.append(i)
        m = i + 2
        if m > n: break
        if isPrime(m): ps.append(m)
        i += 6
    return ps
