'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
Link: https://projecteuler.net/problem=49'''

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

#Build a solve function
def solve():
    #Declare variables
    start = time.time()
    ps, ans, i = [], '', 10**3 + 1
    
    #Solve the problem
    while i < 10**4 - (3330 * 2):
        if isPrime(i):
            if isPrime(i + 3330):
                if isPrime(i + (3330 * 2)):
                    ps.append([i, i + 3330, i + (3330 * 2)])
        if i % 6 == 5: i += 2
        else: i += 4
            
    for i in ps:
        a = sorted(str(i[0]))
        b = sorted(str(i[1]))
        c = sorted(str(i[2]))
        if a == b == c:
            temp = str(i[0]) + str(i[1]) + str(i[2])
            if temp != '148748178147':
                ans = temp

    #Print the results
    print('The 12-digit number formed by concatenating ')
    print('the three terms in this sequence is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
solve()
