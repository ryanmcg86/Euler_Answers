'''An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
Link: https://projecteuler.net/problem=40'''

#Imports
import time

#Build a Champernowne function
def Champernowne():
    start = time.time()
    
    num = ''
    i = 1
    while len(num) < 1000000:
        num += str(i)
        i += 1
    
    ans = 1
    for i in range(0, 7):
        ans *= int(num[10**i - 1])
    
    ans = str(ans)
    
    print 'The value of the given expression is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
Champernowne()
