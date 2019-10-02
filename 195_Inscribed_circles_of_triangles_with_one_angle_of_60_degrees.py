'''Let's call an integer sided triangle with exactly one angle of 60 degrees a 60-degree triangle.
Let r be the radius of the inscribed circle of such a 60-degree triangle.

There are 1234 60-degree triangles for which r ≤ 100.
Let T(n) be the number of 60-degree triangles for which r ≤ n, so
T(100) = 1234,  T(1000) = 22767, and  T(10000) = 359912.

Find T(1053779).
Link: https://projecteuler.net/problem=195'''

#Imports
import time

#Build a gcd function
def gcd(x, y):
    while y != 0:
        a = x
        x = y
        y = a % y
    return x

#Build a Solve function
def solve(n):
    #Define variables
    start = time.time()
    limit = int(2 * n / 3**0.5)
    ans   = 0
  
    #Solve the problem
    for u in range(1, limit + 1):
        v = u + 1
        while u * v - u * u <= limit:
            if (u - v) % 3 != 0 and gcd(u, v) == 1:
                n1 = (v - u) * (v + 2 * u) / 2.0 / 3**0.5
                n2 = u * v * 3**0.5 / 2
                for i in [n1, n2]: 
                    if i <= n: ans += int(n / i) 
            v += 1
	
    ans = str(ans)
    n = str(n)

    #Print the results
    print('T(' + n + ') = ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
n = 1053779
solve(n)
