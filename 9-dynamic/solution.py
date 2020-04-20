# Given n, how many structurally unique BST’s exist that store values 1,..,n?
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

'''
Zain Bhaila
HW9 - Dynamic Programming
04/20/2020

The number of structurallu unique BSTs of size n can be represented by the
Catalan number. So, in order to solve this problem, one must calculate C_n.
Initialize the first value as the base case C_1 to 1. Then loop over the range
of values up to n-1, to calculate the nth Catalan number using the recursive
formula. The formula is C_(n+1) = (2 * (2 * n + 1) * C_(n-1))/(n + 2).

Time Complexity: O(n) - loop executes with proportion to n
Space Complexity: O(1) - stores only the current Catalan value
'''

def num_bsts(n):
    val = 1

    for i in range(1, n): # loop until n values are calculated
        val = ((2 * (2 * i + 1) * val)//(i+2)) # store each calculated value

    return val
