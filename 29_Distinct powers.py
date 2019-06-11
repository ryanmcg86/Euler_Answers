'''Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

2^2 = 4, 2^3 = 8, 2^4 = 16, 2^5 = 32
3^2 = 9, 3^3 = 27, 3^4 = 81, 3^5 = 243
4^2 = 16, 4^3 = 64, 4^4 = 256, 4^5 = 1024
5^2 = 25, 5^3 = 125, 5^4 = 625, 5^5 = 3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
Link: https://projecteuler.net/problem=29'''

#Imports
import time

#Build a answer function
def answer(baseMin, baseMax, expMin, expMax):
    start = time.time()
    
    powers = []
    for a in range(baseMin, baseMax + 1):
        for b in range(expMin, expMax + 1):
            powers.append(a**b)
            
    powers = set(powers)
    
    print 'There are ' + str(len(powers)) + ' distinct terms in the sequence generated by '
    print 'a^b for ' + str(baseMin) + ' <= a <= ' + str(baseMax) + ' and ' + str(expMin) + ' <= b <= ' + str(expMax) + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
baseMin = 2
baseMax = 100
expMin = 2
expMax = 100
answer(baseMin, baseMax, expMin, expMax)
