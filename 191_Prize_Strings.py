'''A particular school offers cash rewards to children with good attendance and punctuality. 
If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?
Link: https://projecteuler.net/problem=191'''

#Imports
import time

#Build a Solve function
def solve(lim):
    #Define variables
    start = time.time()
    f = [1, 2, 4]

    #Solve the problem
    for i in range(3, lim + 1):
        f.append(f[i - 1] + f[i - 2] + f[i - 3])
        
    ans = str(f[lim] + sum([f[i] * f[lim - 1 - i] for i in range(lim)]))
    lim = str(lim)

    #Print the results
    print('There are ' + ans + ' "prize" strings ')
    print('that exist over a ' + lim + '-day period.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
lim = 30
solve(lim)
