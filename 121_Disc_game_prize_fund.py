'''A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. 
After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, 
and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. 
Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, 
so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
Link: https://projecteuler.net/problem=121'''

#Imports
import time

#Build a foil function
def foil(p1, p2):
    result = []
    for i in range(0, len(p1)):
        for j in range(0, len(p2)):
            insert = mult(p1[i], p2[j])
            result.append(insert)
    return result

#Build a multiply function
def mult(p1, p2):
    base = int(p1[0]) * int(p2[0])
    exp  = int(p1[2]) + int(p2[2])
    if p1[1] == 'x' and p2[1] == 'x':
        return [str(base), 'x', str(exp)]
    elif p1[1] == 'x' and p2[1] == '':
        return [str(base), 'x', p1[2]]
    elif p1[1] == '' and p2[1] == 'x':
        return [str(base), 'x', p2[2]]
    elif p1[1] == '' and p2[1] == '':
        return [str(base), '', 1]

#Build a simplify function
def simplify(p1):
    #Find the largest exponent
    maxex = 0
    result = []
    for i in range(0, len(p1)):
        if int(p1[i][2]) > maxex:
            maxex = int(p1[i][2])
    #For each exponent, figure out the base, then add to the result list
    for i in range(maxex, 0, -1):
        base = 0
        for j in range(0, len(p1)):
            if int(p1[j][2]) == i and p1[j][1] == 'x':
                base += int(p1[j][0])
        result.append([str(base), 'x', str(i)])
    #Add the non-x digit at the end
    result.append(p1[len(p1) - 1])
    return result

#Build a solve function
def solve(n):
    #Declare variables
    start = time.time()
    sumOfCoefficients = 0
    fact = 1
    series = []
    for i in range(0, n):
        series.append([['1', 'x', '1'],[str(i + 1), '', '1']])
    result = series[0]
    
    #Solve the problem
    #Build the resultant polynomial with the relevant coefficients
    for i in range(1, len(series)):
        result = foil(result, series[i])
        result = simplify(result)
        
    #Sum up the winning coefficients
    for i in range(0, len(result)):
        if int(result[i][2]) > (n / 2):
            sumOfCoefficients += int(result[i][0])

    #Find the relevant factorial
    for i in range(n + 1, 0, -1):
        fact *= i
                
    #Print the results
    print 'When there are ' + str(n) + ' turns played, the prize fund can '
    print 'go as high as £' + str(fact / sumOfCoefficients) + ' before losing profitability.'
    print 'It took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
n = 15
solve(n)
