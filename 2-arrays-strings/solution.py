# Given an array of size n, where the values are between 1 and n inclusive and
# each value may at most appear twice, return a List of all the duplicate
# elements. All tests have duplicates occur in ascending order (i.e. a duplicate
# 1 would occur before a duplicate 2, etc), so your output MUST have the
# duplicates in ascending order!

"""
Zain Bhaila
02/07/2020
Uses a dictionary to keep track of whether or not a value has already occured
by setting the value to 1 in the dictionary. Do this for each element in nums
and if it already has a value of 1, then add it to the duplicates array.
Returns an array of duplicates in the order they occur.
Time Complexity: O(n) - iterate over nums, dictionary is checked in O(1)
Space Complexity: O(n) - uses both an array and dictionary that are O(n) in size
"""

from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    duplicates = [] # store all duplicate values
    tracker = {} # dict to keep track of seen values
    for i in nums:
        if tracker.get(i) == 1: # if it is a duplicate add it
            duplicates.append(i)
        else: # else mark as seen
            tracker[i] = 1
    return duplicates