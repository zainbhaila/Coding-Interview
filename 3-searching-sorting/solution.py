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

# for student use
EPSILON: float = 1e-6

def student_ln(x: float) -> float:
    return 0 # TODO implement
