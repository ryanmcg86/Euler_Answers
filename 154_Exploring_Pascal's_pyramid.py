'''A triangular pyramid is constructed using spherical balls so that each ball rests on exactly 
three balls of the next lower level.


Then, we calculate the number of paths leading from the apex to each position:

A path starts at the apex and progresses downwards to any of the three spheres directly below the current position.

Consequently, the number of paths to reach a certain position is the sum of the numbers immediately above it 
(depending on the position, there are up to three numbers above it).

The result is Pascal's pyramid and the numbers at each level n are the coefficients of the trinomial expansion (x + y + z)^n.

How many coefficients in the expansion of (x + y + z)^200000 are multiples of 10^12?
Link: https://projecteuler.net/problem=154'''

#Imports
import time

#Build a pows function
def pows(n, p):
    amount = 0
    powp = p
    while powp <= n:
        amount += n / powp
        powp *= p
    return amount
    
#Build a perms function
def perms(a, b, c):
    if a == b:
        if b == c:
            return 1
        else:
            return 3
    elif a == c:
        return 3
    elif b == c:
        return 3
    else:
        return 6
   
#Build a Solve function
def solve(exp):
    #Define variables
    start = time.time()
    fivepows = []
    twopows = []
    five = pows(exp, 5)
    two = pows(exp, 2)
    ans = 0
    
    #Solve the problem
    for i in range(exp + 1):
        fivepows.append(pows(i, 5))
        twopows.append(pows(i, 2))
	
    for a in range(exp + 1):
        b = a
        c = exp - (b + a)
        while b <= c:
            pow5 = fivepows[a] + fivepows[b] + fivepows[c]
            pow2 = twopows[a] + twopows[b] + twopows[c]
            if five - pow5 >= 12 and two - pow2 >= 12:
                ans += perms(a, b, c)
            b += 1
            c -= 1

    
    #Print the results
    print 'There are ' + str(ans) + ' coefficients in the expansion of '
    print '(x + y + z)^' + str(exp) + ' that are multiples of 10^12.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
exp = 200000
solve(exp)
