'''
Zain Bhaila
Problem 2
Given the root of a binary tree, verify that the tree is a binary search tree

This can be done by checking that the left node is less than and the right node
is greater than the root. Do this recursively. This will run in O(n) time as it
will do this process for every node. It will also take O(n) space since space on
the stack is needed for recursion.
'''

class Node:
    def __init__(self, data, left, right): # left and right are nodes
        self.data = data
        self.left = left
        self.right = right
        return

def verify(n): # n is a Node
    if (n.left == None and n.right == None): # node is a leaf
        return True
    elif (n.left == None): # node only has right child
        if (n.right.data > n.data):
            return verify(n.right)
        else:
            return False
    elif (n.right == None): # node only has left child
        if (n.left.data < n.data):
            return verify(n.left)
        else:
            return False
    else: # both children are present
        if (n.left.data < n.data and n.right.data > n.data):
            return verify(n.left) and verify(n.right)
        else:
            return False
