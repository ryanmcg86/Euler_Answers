'''Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
(i.e. 0 ≤ yi < 2^32, every value equally likely).

For the sequence xi the following recursion is given:

x0 = 0 and
xi = xi-1| yi-1, for i > 0. ( | is the bitwise-OR operator)
It can be seen that eventually there will be an index N such that xi = 2^32 - 1 (a bit-pattern of all ones) for all i ≥ N.

Find the expected value of N.
Give your answer rounded to 10 digits after the decimal point.
Link: https://projecteuler.net/problem=323'''

#Imports
import time
from decimal import *

#Build a Solve function
def solve(digits, bits):
    #Define variables
    start = time.time()
    getcontext().prec = (digits + 3)
    ans, n, a = Decimal(0), 0, '0.0'
    prev = a[a.index('.') + 1 : a.index('.') + 1 + digits]
    curr, last = '9' * digits, ''
    
    #Solve the problem
    while prev != curr:
        prev = curr
        ans += Decimal(1 - ((2**n - 1) / (2**n))**bits)
        a = str(ans)
        if '.' in a: begin = a.index('.') + 1
        else: begin = 0
        curr = a[begin : begin + digits]
        n += 1
        
    getcontext().rounding = ROUND_CEILING
    num, digits, bits = '1.' + '0' * digits, str(digits), str(bits)
    ans = str(Decimal(str(ans)).quantize(Decimal(num)))
    
    #Print the results
    print('Given a sequence of random unsigned ' + bits + '-bit ')
    print('integers, the expected value of N, rounded to ' + digits)
    print('decimal places, is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
digits, bits = 10, 32
solve(digits, bits)
