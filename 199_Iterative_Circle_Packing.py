'''Three circles of equal radius are placed inside a larger circle such that each pair of circles is tangent to 
one another and the inner circles do not overlap. There are four uncovered "gaps" which are to be filled iteratively 
with more tangent circles.

At each iteration, a maximally sized circle is placed in each gap, which creates more gaps for the next iteration. 
After 3 iterations (pictured), there are 108 gaps and the fraction of the area which is not covered by circles is 0.06790342, 
rounded to eight decimal places.

What fraction of the area is not covered by circles after 10 iterations?
Give your answer rounded to eight decimal places using the format x.xxxxxxxx .
Link: https://projecteuler.net/problem=199'''

#Imports
import time

#Build an inner circle function
def inner_circle(k1, k2, k3):
    x1 = k1 + k2 + k3
    x2 = k1**2 + k2**2 + k3**2
    b, c = -2 * x1, 2 * x2 - x1**2
    return (-b + (b**2 - 4 * c)**0.5) / 2

#Build a Solve function
def solve(iterations):
    #Define variables
    start = time.time()
    k0 = (2 + 3**0.5) / 3**0.5
    curr = [(k0, k0, -1), (k0, -1, k0), (-1, k0, k0), (k0, k0, k0)]
    area_rem = 1 - 3 / k0**2
  
    #Solve the problem
    for i in range(iterations):
        next_list = []
        for (k1, k2, k3) in curr:
            k = inner_circle(k1, k2, k3)
            area_rem -= 1 / k**2
            next_list.extend([(k1, k2, k), (k2, k3, k), (k1, k3, k)])
        curr = next_list
	
    ans = str(round(area_rem, 8))
    i = str(iterations)

    #Print the results
    print('After ' + i + ' iterations, there is ' + ans + ' area remaining.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
iterations = 10
solve(iterations)
