'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
Link: https://projecteuler.net/problem=3'''

#Imports
import time

#Build a factors function
def factors(n):
    factors = []
    for i in range(2, 4):
        while n % i == 0:
            factors.append(i)
            n /= i
    for i in range(5, int(n**0.5) + 1, 6):
        plus2 = [i, i + 2]
        for j in plus2:
            while n % j == 0:
                factors.append(j)
                n /= j
    if n > 2:
        factors.append(n)
    return factors

#Largest prime factor function
def lpf(n):
    #Declare variables
    start = time.time()
    
    #Solve the problem
    ans = str(factors(n)[-1])
    n = str(n)
    
    #Print the results
    print 'The largest prime factor of ' + n + ' is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 600851475143
lpf(n)
