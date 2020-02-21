# Given the reference to the head of singly LinkedList, develop an algorithm
# that detects if there exists a cycle. A cycle is defined as one of the nodes
# pointing to a previous node in the array. Thus, if we traversing the array,
# we would never know when the traversal ends.

"""
Zain Bhaila
2/21/2020
Uses a slow and fast pointer to traverse the list. Move the slow pointer by 1
and the fast pointer by 2. If they are ever the same then there is a cycle
because the fast pointer has looped back around and caught up to the slow
pointer. If there isn't a cycle, the fast pointer will reach None before
the slow pointer and the loop will end.

Time Complexity: O(n) - traverse the list simultaneously with two pointers
Space Complexity: O(1) - doesn't use any other data structures
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def hasCycle(head: Node) -> bool:
    slow = head # slow pointer
    fast = head # fast pointer
    while slow != None and fast != None and fast.next != None: # traverse list
        slow = slow.next # move slow pointer by 1
        fast = fast.next.next # move fast pointer by 2
        if slow == fast: # cycle found here
            return True
    return False
