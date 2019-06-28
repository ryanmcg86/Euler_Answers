'''The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 ×  7 × 23
645 = 3   ×  5 × 43
646 = 2   × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
Link: https://projecteuler.net/problem=47'''

#Imports
import time

#Build a prime_factors_count function
def pfc(n):
    factors = []
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n /= 2
    if n % 3 == 0:
        factors.append(3)
        while n % 3 == 0:
            n /= 3
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n /= i
        if n % (i + 2) == 0:
            factors.append(i + 2)
            while n % (i + 2) == 0:
                n /= (i + 2)
    if n > 2:
        factors.append(n)
    return len(factors)

#Build a solve function
def solve(consecNums):
    #Declare variables
    start    = time.time()
    notfound = True
    alltrue  = True
    ans      = 1

    #Solve the problem
    while notfound:
        ans += 1
        for i in range(0, consecNums):
            if pfc(ans + i) != consecNums:
                alltrue = False
                break
            alltrue = True
        if alltrue == True:
            notfound = False

    #Print the results
    print 'The first number of the first ' + str(consecNums) + ' consecutive integers '
    print 'to have ' + str(consecNums) + ' distinct prime factors each is ' + str(ans) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
consecNums = 4
solve(consecNums)
