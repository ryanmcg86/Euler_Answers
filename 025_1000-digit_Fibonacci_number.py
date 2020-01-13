'''The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
Link: https://projecteuler.net/problem=25'''

#Imports
import time

#Build a find-nth-index function, where the nth
#index is the first Fibonacci # with an inputted
#amount of digits
def findIndex(digits):
    #Declare variables
    start = time.time()
    fib, ans = [1, 1], 1
    
    #Solve the problem
    while fib[0] // 10**(digits - 1) < 1:
        fsum = sum(fib)
        fib[0] = fib[1]
        fib[1] = fsum
        ans += 1
        
    ans, d = str(ans), str(digits)
        
    #Print the results
    print('The index of the first term in the Fibonacci ')
    print('sequence to contain ' + d + ' digits is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
digits = 1000
findIndex(digits)
