'''An electric circuit uses exclusively identical capacitors of the same value C. 
The capacitors can be connected in series or in parallel to form sub-units, 
which can then be connected in series or in parallel with other capacitors or other 
sub-units to form larger sub-units, and so on up to a final circuit.

Using this simple procedure and up to n identical capacitors, we can make circuits having 
a range of different total capacitances. For example, using up to n=3 capacitors of 60 F each, 
we can obtain the following 7 distinct total capacitance values:


If we denote by D(n) the number of distinct total capacitance values we can obtain when using 
up to n equal-valued capacitors and the simple procedure described above, we have: 
D(1) = 1, D(2) = 3, D(3) = 7 ...

Find D(18).

Reminder : When connecting capacitors C1, C2 etc in parallel, the total capacitance is CT = C1 + C2 + ..., 
whereas when connecting them in series, the overall capacitance is given by: 1 / CT = (1 / C1) + (1 / C2) + ...
Link: https://projecteuler.net/problem=155'''

#Imports
import time
   
#Build a Solve function
def solve(limit):
    #Define variables
    start = time.time()
    unit = 100000000000.0
    caps_n = {1 : [unit]}
    caps_all = set([int(unit)])
    
    #Solve the problem
    for i in range(2, limit + 1):
        caps_n[i] = []
        for j in range(1, i / 2 + 1):
            for c1 in caps_n[j]:
                for c2 in caps_n[i - j]:
                    for x in [c1 + c2, c1 * c2 / (c1 + c2)]:
                        if int(x + 0.5) not in caps_all:
                            caps_all.add(int(x + 0.5))
                            caps_n[i].append(x)
	
    ans = str(len(caps_all))

    
    #Print the results
    print 'If we denote by D(n) the number of distinct total '
    print 'capacitance values we can obtain when using up to n '
    print 'equal-valued capacitors and the simple procedure '
    print 'described in the problem, D(' + str(limit) + ') = ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
limit = 18
solve(limit)
