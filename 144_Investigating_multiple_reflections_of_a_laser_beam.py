'''In laser physics, a "white cell" is a mirror system that acts as a delay line for the laser beam. 
The beam enters the cell, bounces around on the mirrors, and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation 4x2 + y2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to enter and exit through the hole.


The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, 
and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual law of reflection 
"angle of incidence equals angle of reflection." That is, both the incident and reflected beams make the 
same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between the laser beam and 
the wall of the white cell; the blue line shows the line tangent to the ellipse at the point of incidence of the 
first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = −4x / y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?
Link: https://projecteuler.net/problem=144'''

#Imports
import time
    
#Build a Solve function
def solve():
    #Define variables
    start = time.time()
    result = 0
    xA = 0.0
    yA = 10.1
    xO = 1.4
    yO = -9.6
    
    #Solve the problem
    while xO > 0.01 or xO < -0.01 or yO < 0:
        slopeA = (yO - yA) / float(xO - xA)
        slopeO = -4 * xO / float(yO)
        tanA = (slopeA - slopeO) / float(1 + slopeA * slopeO)
        slopeB = (slopeO - tanA) / float(1 + tanA * slopeO)
        interceptB = yO - slopeB * xO
        a = 4 + slopeB**2
        b = 2 * slopeB * interceptB
        c = interceptB**2 - 100
        ans1 = (-b + (b**2 - 4 * a * c)**0.5) / float(2 * a)
        ans2 = (-b - (b**2 - 4 * a * c)**0.5) / float(2 * a)
        xA = xO
        yA = yO
        if abs(ans1 - xO) > abs(ans2 - xO):
            xO = ans1
        else:
            xO = ans2
        yO = slopeB * xO + interceptB
        result += 1
	
    ans = str(result)

    #Print the results
    print 'The beam hit the internal surface of '
    print 'the white cell ' + ans + ' times before exiting.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
solve()
