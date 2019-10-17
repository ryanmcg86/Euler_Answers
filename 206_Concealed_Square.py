'''Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
Link: https://projecteuler.net/problem=206'''

#Imports
import time

#Build a match function
def match(n):
    s = str(n)
    return not all(int(s[x * 2]) == x + 1 for x in range(9))

#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    n = int(19293949596979899**0.5) + 1

    #Solve the problem
    while match(n**2):
        if n % 10 == 3:
            n -= 6
        else:
            n -= 4
        
    ans = str(n * 10)

    #Print the results
    print('The unique positive integer whose square ')
    print('has the form 1_2_3_4_5_6_7_8_9_0, where each ')
    print('"_" is a single digit, is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
solve()
