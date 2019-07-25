'''The proper divisors of a number are all the divisors excluding the number itself. 
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, 
we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, 
forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
Link: https://projecteuler.net/problem=95'''

#Imports
import time

#Build an isPrime function
def isPrime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
#Build a build_sieve function
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

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    sums = [1] * (limit + 1)
    longest = 0
    done = set(build_sieve(limit))
    todo = set(range(4, limit + 1)) - done
    
    #Solve the problem
    for n in range(2, limit / 2 + 1):
        for i in range(2 * n, limit + 1, n):
            sums[i] += n
            
    while todo:
        n = todo.pop()
        new = n
        seen = [n]
        while True:
            new = sums[new]
            todo.discard(new)
            if new == False or new in done or new > limit:
                done.update(set(seen))
                break
            if new in seen:
                chain = seen[seen.index(new):]
                length = len(chain)
                if length > longest:
                    longest = length
                    best = min(chain)
                done.update(set(seen))
                break
            seen.append(new)
    
    #Print the results
    print 'The smallest member of the longest amicable chain '
    print 'with no element exceeding ' + str(limit) + ' is ' + str(best) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
limit = 10**6
solve(limit)
