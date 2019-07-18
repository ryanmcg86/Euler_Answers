'''Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an 
integer with (1,2, ... , n) where n > 1?
Link: https://projecteuler.net/problem=38'''

#Imports
import time

#Build an isPandigital function
def isPan(n):
    num = ''.join(str(i) for i in range(1, len(str(n)) + 1))
    return num == ''.join(sorted(str(n)))

#Build a Solve function
def Solve():
    start = time.time()
    
    values   = []
    largest  = 0
    maxindex = 0
    
    #We go as high as 4 digits b/c n must
    #be at least 2, and concatenating two
    #five digit numbers will make a 10-digit
    #number, and it must be 9-digits to be
    #pandigital.
    for i in range(1, 10000):
        num = ''
        #We only go to 9 b/c when i is 1,
        #we can multiple to n = 9 for the 
        #smallest pandigital. This sets our
        #upper bound.
        for j in range(1, 10):
            num += str(i * j)
            if isPan(int(num)):
                values.append([i, j, int(num)])
                
    for i in range(0, len(values)):
        if values[i][2] > largest:
            maxindex = i
            largest = values[i][2]
            
    a = str(values[maxindex][0])
    b = str(values[maxindex][1])
    c = str(values[maxindex][2])
    
    print 'The concatenated product of ' + a + ' and 1 through ' + b + ' is ' + c + ', '
    print 'which is the largest 1 to 9 pandigital 9-digit number that can be formed  '
    print 'as the concatenated product of an integer with (1,2, ... , n) where n > 1.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
Solve()
