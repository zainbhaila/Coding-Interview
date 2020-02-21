# Given the reference to the head of singly LinkedList, develop an algorithm
# that detects if there exists a cycle. A cycle is defined as one of the nodes
# pointing to a previous node in the array. Thus, if we traversing the array,
# we would never know when the traversal ends.

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def hasCycle(head: Node) -> bool:
    # TODO
