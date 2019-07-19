'''A natural number, N, that can be written as the sum and product of a given set of at least 
two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. 
The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k = 2: 4 = 2 × 2 = 2 + 2
k = 3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k = 4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k = 5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k = 6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2 ≤ k ≤ 6, the sum of all the minimal product-sum numbers is 4 + 6 + 8 + 12 = 30; 
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2 ≤ k ≤ 12000?
Link: https://projecteuler.net/problem=88'''

#Imports
import time

#Build a solve function
def solve(limit):
    #Define variables
    start = time.time()
    kmax = limit
    def prodsum(prod, sum, factorCount, start):
        k = prod - sum + factorCount
        if k < kmax:
            if prod < n[k]:
                n[k] = prod
            for i in range(start, kmax // prod * 2 + 1):
                prodsum(prod * i, sum + i, factorCount + 1, i)

    if kmax > 12:
        kmax += 1
    n = [2 * kmax] * kmax

    #Solve the problem	
    prodsum(1, 1, 1, 2)
	
    ans = str(sum(set(n[2:])))

    #Print the results
    print 'The sum of all the minimal product-sum '
    print 'numbers for 2 <= k <= ' + str(limit) + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds too calculate.'

#Run the program
limit = 12000
solve(limit)
