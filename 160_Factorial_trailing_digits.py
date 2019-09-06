'''For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

 9! = 362880  so f(9)  = 36288
10! = 3628800 so f(10) = 36288
20! = 2432902008176640000 so f(20) = 17664

Find f(1,000,000,000,000)
Link: https://projecteuler.net/problem=160'''

#Imports
import time
   
#Build a Solve function
def solve(limit, digits):
    #Define variables
    start = time.time()
    result = 1
    n = 2560000
    i = 1
    
    #Solve the problem
    while i <= n:
        result *= i
        while result % 10 == 0:
            result /= 10
        result %= limit
        i += 1
            
    ans = str(result % 10**digits)
    lim = str(limit)
        
    #Print the results
    print 'f(' + lim + ') = ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**12
digits = 5
solve(limit)
