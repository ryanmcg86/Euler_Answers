'''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
Link: https://projecteuler.net/problem=39'''

#Imports
import time

#Build a Solve function
def Solve(num):
    start = time.time()
    
    perimeters = [0] * (num + 1)
    
    for a in range(1, num / 3 + 1):
        for b in range(a + 1, num / 2):
            c = int((a**2 + b**2)**0.5)
            if a**2 + b**2 == c**2 and a + b + c <= num:
                perimeters[a + b + c] += 1
                
    per = 0
    
    for i in range(0, len(perimeters)):
        if perimeters[i] == max(perimeters):
            per = i
            break
        
    per = str(per)
    
    print 'The value for which p <= ' + str(num) + ' is maximized is ' + per + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
num = 1000
Solve(num)
