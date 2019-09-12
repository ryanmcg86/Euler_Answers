'''We shall define a square lamina to be a square outline with a square "hole" so that the 
shape possesses vertical and horizontal symmetry. For example, using exactly thirty-two square 
tiles we can form two different square laminae:

                 * * * * * *         * * * * * * * * *
                 * * * * * *         *               *
                 * *     * *         *               *
                 * *     * *         *               *
                 * * * * * *         *               *
                 * * * * * *         *               *
                                     *               *
                                     *               *
                                     * * * * * * * * *

With one-hundred tiles, and not necessarily using all of the tiles at one time, it is possible to 
form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?
Link: https://projecteuler.net/problem=173'''

#Imports
import time
   
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    tot = 0
    tiles = limit / 4
    end = int(tiles**0.5) + 1
    
    #Solve the proble
    for i in range(1, end):
        tot += (tiles / i) - i
        
    lim = str(limit)
    ans = str(tot)
        
    #Print the results
    print 'Using up to ' + lim + ' tiles, '
    print ans + ' square laminae can be formed.' 
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 10**6
solve(limit)
