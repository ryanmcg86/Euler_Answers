'''The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
Link: https://projecteuler.net/problem=37'''

#Imports
import time

#Build an isPrime function
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
#Build an isTruncatable function
def isTruncatable(n):
    if isPrime(n) == False:
        return False
    num = str(n)[1:]
    while num != '':
        if isPrime(int(num)) == False:
            return False
        num = num[1:]
    num = str(n)[:-1]
    while num != '':
        if isPrime(int(num)) == False:
            return False
        num = num[:-1]
    return True

#Build a Solve function
def Solve(num):
    start = time.time()
    total = 0
    count = 0
    i = 11
    while count < 11:
        if isTruncatable(i):
            count += 1
            total += i
        if isTruncatable(i + 2):
            count += 1
            total += (i + 2)
        i += 6
            
    total = str(total)
    
    print 'The sum of the only eleven primes that are both truncatable'
    print 'from left to right and right to left is ' + total + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
Solve()
