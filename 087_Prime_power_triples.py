'''The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
Link: https://projecteuler.net/problem=87'''

#Imports
import time
    
#Build a prime sieve function
def SoE(n):
	prime = [False] * 2 + [True for i in range(n - 1)]
	ans, p = [], 2
	while p**2 <= n:
		if prime[p]:
			for i in range(p * 2, n + 1, p):
				prime[i] = False
		p += 1
	return [i for i in range(n) if prime[i]]

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    primes, ans = [], set()
    
    #Update sieves with the primes raised to the correct exponent
    for i in range(4, 1, -1):
        primes.append(SoE(int(limit**(1 / float(i)))))
        primes[-1] = [j**i for j in primes[-1]]

    #Solve the problem
    for i in primes[0]:
        for j in primes[1]:
            ij = i + j
            if ij >= limit: break
            for k in primes[2]:
                num = ij + k
                if num < limit:
                    nums.add(num)
                else: break
                    
    ans, lim = str(len(ans)), str(limit)

    #Print the results
	print('The amount of numbers that can be expressed ')
	print('as the sum of a prime square, prime cube, and ')
	print('prime fourth power while being less than ' + lim + ' is ' + ans + '.')
	print('This took ' + str(time.time() - start) + ' seconds too calculate.')

#Run the program
limit = 5 * 10**7
solve(limit)
