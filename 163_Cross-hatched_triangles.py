'''Consider an equilateral triangle in which straight lines are drawn from each vertex to the 
middle of the opposite side.

Sixteen triangles of either different shape or size or orientation or location can now be observed 
in that triangle. Using size 1 triangles as building blocks, larger triangles can be formed. 
One-hundred and four triangles of either different shape or size or orientation or location can now 
be observed in that size 2 triangle.

It can be observed that the size 2 triangle contains 4 size 1 triangle building blocks. A size 3 
triangle would contain 9 size 1 triangle building blocks and a size n triangle would thus contain 
n^2 size 1 triangle building blocks.

If we denote T(n) as the number of triangles present in a triangle of size n, then

T(1) = 16
T(2) = 104

Find T(36).
Link: https://projecteuler.net/problem=163'''

#Imports
import time
   
#Build a Solve function
def T(n):
    #Define variables
    start = time.time()
    a = 1678  *   n**3
    b = 3117  *   n**2
    c =   88  *   n
    d =  345  *  (n % 2)
    e =  320  *  (n % 3)
    f =   90  *  (n % 4)
    g =  288  * ((n**3 - n**2 + n) % 5)
    
    #Solve the proble
    ans = str((a + b + c - d - e - f - g) / 240)
    n = str(n)
        
    #Print the results
    print 'If we denote T(n) as the number of triangles '
    print 'present in a triangle of size n, T(' + n + ') = ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
n = 36
T(n)
