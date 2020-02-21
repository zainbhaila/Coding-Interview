# CMSC389O Spring 2020
# HW3: Searching & Sorting -- Implement Natural Logarithm

# Description:
# Implement the ln() function, but don't use the library log functions or integration functions.
# Other library functions are fine
# Solutions should be within 1e-6 of the actual value (i.e. |student_ln(x) - ln(x)| < 1e-6)

# Hints:
# - This is for the sorting and searching section of the course. Don't use integration or bit manipulation.
# - What if you were given a sorted list of values where at least one of them were guaranteed to be acceptable?
# - ln() is (strictly) monotonically increasing -- i.e. for x < y in the domain, ln(x) < ln(y)

# Examples:
# 2.718281828459045 -> 1 (or anything within 1e-6 of 1)
# 20.085536923187668 -> 3 (or anything within 1e-6 of 3)

# Edge cases:
# ln(0) should return the floating point negative infinity float('-inf')
# ln(x) for negative x should raise ValueError (it's an invalid input)

# Running the public tests:
# python3 PublicTests.py

# Submit server notes:
# 2 of the release tests (9 and 10) are performance tests.
# Failing either of the last 2 tests (red box) is probably not due to
# correctness issues if you are passing the other tests.

"""
Zain Bhaila
02/17/2020
Bases cases check for 0 and negative inputs.
Create an initial approximation to center the binary search around using
an identity for the natural log. Approximation is good enough that we only
need to search with a radius of .0015 to find a better approximation. Do a
binary search over all values within the radius, increasing the lower bound if
our approximation is low, and decreasing the upper bound if our approximation
is high. Stop the approximation when our change in values is no longer
significant (when the difference is within the desired accuracy).

Time Complexity: O(1) - Binary search always occurs in a range of .003, so it
    executes in constant time. Approximation also occurs in constant time.
Space Complexity: O(1) - No data structures are used.
"""

# needed for 'e' value
import math

# for student use
EPSILON: float = 1e-6

def student_ln(x: float) -> float:
    if x == 0: # base cases
        return float('-inf')
    if x < 0:
        raise ValueError("Invalid Input")

    n = 99999999 * ((x ** (1/99999999)) - 1) # actual identity is a limit, but this is good start 
    l = n - .0015 # binary search based algorithm
    r = n + .0015
    mid = n
    previous = -1
    while True: # search near the solution until approximation is good
        if math.exp(mid) > x: # current value is too large
            r = mid
            mid = (l+r)/2
        else: # current value is too small
            l = mid
            mid = (l+r)/2
        if abs(mid - previous) < EPSILON: # check if approximation is good
            break; # stop looping when a close approximation has been found
        previous = mid
    return mid
