'''A common security method used for online banking is to ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest 
possible secret passcode of unknown length.
Link: https://projecteuler.net/problem=79'''

#Imports
import time
from itertools import permutations as p

#Build a solve function
def solve(name):
    #Define variables
    start = time.time()
    digits = set()
    ans = 0
    f = open(name, 'r')
    keys = f.read().split('\n')
    keys = [list(key) for key in keys if len(key) > 0]
    for i in range(0, len(keys)):
        keys[i] = [int(num) for num in keys[i]]
    for key in keys:
        for digit in key:
            digits.add(digit)
    digits = list(digits)
    perms = p(digits)
    
    #Solve the problem
    for perm in perms:
        valid = True
        for key in keys:
            if valid:
                a = perm.index(key[0])
                b = perm.index(key[1])
                c = perm.index(key[2])
                if a > b or b > c:
                    valid = False
                    break
        if valid:
            ans = ''.join(str(i) for i in perm)
            break
    
    #Print the results
    print 'The shortest possible secret passcode of unknown length is ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
name = 'keylog.txt'
solve(name)
