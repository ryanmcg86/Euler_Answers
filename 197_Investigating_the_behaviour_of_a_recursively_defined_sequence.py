'''Given is the function f(x) = ⌊230.403243784-x2⌋ × 10-9 ( ⌊ ⌋ is the floor-function),
the sequence un is defined by u0 = -1 and un+1 = f(un).

Find un + un+1 for n = 10^12.
Give your answer with 9 digits after the decimal point.
Link: https://projecteuler.net/problem=197'''

#Imports
import time

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
    k = 30.403243784
    mod = 10**-9
    x = last_sum = -1
  
    #Solve the problem
    while True:
        y, x = x, int(pow(2, k - x**2)) * mod
        next_sum = x + y
        if last_sum == next_sum:
            ans = str(last_sum)
            break
        last_sum = next_sum
        
    lim = str(lim)

    #Print the results
    print('U(n) + U(n + 1) for n = ' + lim + ' = ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 10**12
solve(lim)
