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

from typing import List

def evalRPN(tokens: List[str]) -> int:
    # TODO
