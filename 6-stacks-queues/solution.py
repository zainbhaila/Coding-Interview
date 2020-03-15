# Given a list of strings containing integers and arithmetic operators ordered
# by reverse polish notation, evaluate the expression.
# Valid operators are +, -, *, / .
# We will use truncated integer division here. For example, 13/6 = 2.
# Also, whenever we have [operand1 operand2 operator], operand 1 always comes first.
# So, [“7” “2”,  “-”] is  7 - 2, and [“13”, “6”, “/”] is 13/6.
# For this question, you will get only +, *, -, and /, and have no invalid inputs.
# All lists will be in appropriate RPN order. If an empty list is provided, return 0.
# Return all outputs as integers (not strings)

# How it works
# In reverse polish notation, operators are put after the operands. So for example,
# instead of writing 3 + 4, we write 3 4 +. The steps to evaluating an RPN expression
# are as follows.

# 1. Evaluate operators left to right. Starting with the leftmost operator,
# 2. Given the operator you’re currently on, apply it to the two operands directly
#    before it. Remove the operator and its operands , and replace them with the result.
# 3. Repeat step one with the next operator on the left hand side, if there is one.
#    Otherwise, the final result is your answer.

"""
Zain Bhaila
03/15/2020
The three function takes three strings, two numeric and one operand and uses
the operand on the given values. O(1) time and space.
My implementation uses a stack to keep track of integers. It loops through the
given list of tokens. If it is an integer it gets added to the stack. Otherwise,
I apply the three function to the top two values in the stack and the current
operand. Add the new value to the top of the stack and proceed. At the end,
there will only be one value in the stack and none in tokens. Return the value
in the stack.

Time Complexity: O(n) - goes through each element in input once
Space Complexity: O(n) - uses an additional List as a stack, up to the size of the input
"""

from typing import List
import re

def three(val1, val2, operand): # takes two numbers and an operand string and applies the operand
    val1 = int(val1) # convert inputs to int
    val2 = int(val2)

    if operand ==  # determine the operand and return correct value
        return val1 + val2
    elif operand == "-":
        return val2 - val1
    elif operand == "*":
        return val1*val2
    elif operand == "/":
        return val2//val1 # integer division

def evalRPN(tokens: List[str]) -> int:
    stack = []
    while (len(tokens) >= 1): # loop until all tokens are consumed
        current = tokens.pop(0)
        if (re.search("-?[0-9]+", str(current)) != None): # if integer, add to stack
            stack.append(current)
        else: # if token is operand, replace top two values in stack with operated values
            replacement = three(stack.pop(), stack.pop(), current)
            stack.append(replacement)
    return stack.pop()
