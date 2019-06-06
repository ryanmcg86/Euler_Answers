'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
Link: https://projecteuler.net/problem=3'''

#Imports
import time

#isPrime function
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    while i * i <= n:
        if n % i == 0 or n % (n + 2) == 0:
            return False
        i += 6
    return True

#Largest prime factor function
def lpf(n):
    start = time.time()
    result = 1
    while n % 2 == 0:
        n /= 2
        result = n
    begin = int(n**0.5)
    if begin % 2 == 0:
        begin -= 1
    for i in range(begin, 1, -2):
        if isPrime(i) and n % i == 0:
            result = i
            break
    print 'The largest prime factor of ' + str(n) + ' is ' + str(result) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 600851475143
lpf(n)
