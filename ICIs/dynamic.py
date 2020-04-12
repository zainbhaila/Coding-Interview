'''
Zain Bhaila
ICI #1
Skip-onacci

Given n, return the nth "skip-onacci" number. The skip-onacci series is a modification of the 
Fibonacci sequence where each term is the sum of the first and third previous terms. 
The sequence goes as follows: 0, 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189, ...

First, create array with first three values and return if n is one of those.
Then create a loop to calculate the skip-onacci of the nth number. Do this
by calculating the new value, adding it to storage, and then remove the value that
is now the fourth previous term.
Time: O(n) - one loop over n
Space: O(1) - only max of four data points stored at any given time
'''

def skip(n):
    values = [0;1;1]
    if n <= 3:
        return values[n - 1]
    for i in range(n-3): # first three values already calculated
        values.append(values[0]+values[2])
        values.pop(0)
    return values[2]