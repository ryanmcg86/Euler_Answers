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
    
#Build an add-the-next-Fibonacci-number function
def addFib(fib):
    size = len(fib)
    a = fib[size - 1]
    b = fib[size - 2]
    fib.append(a + b)
    
 #Build a most-recent-fib-term's-length function
 def mrftl(fib):
     return len(str(fib[len(fib) - 1]))

#Build a find-nth-index function, where the nth
#index is the first Fibonacci # with an inputted
#amount of digits
def findIndex(fib, digitlen):
    start = time.time()
    
    while mrftl(fib) < digitlen:
        addFib(fib)
        
    print 'The index of the first term in the Fibonacci sequence '
    print 'to contain ' + str(digitlen) + ' digits is ' + str(len(fib)) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
fib = [1, 1]
digitlen = 1000
findIndex(fib, digitlen)
