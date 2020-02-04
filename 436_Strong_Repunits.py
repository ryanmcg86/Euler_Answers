'''The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6
(i.e. 7 in base 10 = 11 in base 6 = 111 in base 2). 
In other words, 7 is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit. 
It can be verified that there are 8 strong repunits below 50: {1, 7, 13, 15, 21, 31, 40, 43}.
Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 10^12.
Link: https://projecteuler.net/problem=346'''

#Imports
import time

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
    found, b = {1}, 2
   
    #Solve the problem
    while b**2 < lim:
        curr = 1 + b + b * b
        pows = b * b
        while curr < lim:
            found.add(curr)
            pows *= b
            curr += pows
        b += 1
        
    ans, lim = str(sum(found)), str(lim)
    
    #Print the results
    print('The sum of all strong repunits below ' + lim + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 10**12
solve(lim)
