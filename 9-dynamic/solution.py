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


def num_bsts(n):
    # TODO
