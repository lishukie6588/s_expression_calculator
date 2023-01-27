## Shukie Li
## lishukie1988@gmail.com
## +1 647 686 3849

## Solution to S-expression calculator
## Space Complexity: O(n) where n = number of characters in expression
# - allows any number of values for each operation expression
# - allows the following operations:
#   - addition
#   - multiplication
#   - exponent
# - easily expandable for more operations
# - includes error handling for invalid operator
# - concretely documented methods


import math
import sys

class Solution:


    # contains the input terminal expression
    arguments = sys.argv[1]


    # - Prints:
    #   - solution to the terminal input expression
    #   - input follows grammar specified in the given document
    #   - takes in 2 or more values for each expression
    #   - does the following operations: addition, multiplication, exponent
    # - Parameters: none
    # - Return value: none
    def parse(self):

        if self.arguments[0] != '(':
            print(int(sys.argv[1]))
            return
        print(self.recursion(0)[0])


    # - Parameters:
    #   - int Index: starting index of an input expression
    # - Return value:
    #   - tuple containing:
    #     - int: evaluated value to an input expression surrounded by a pair of parantheses
    #     - int: index following closing paranthesis of input expression)
    def recursion(self, index):

        endOfOperator = self.arguments.find(" ", index)
        operator = self.arguments[index + 1: endOfOperator]
        index = endOfOperator + 1
        values = []
        currentInteger = 0

        while index < len(self.arguments) and self.arguments[index] != ')':
            currentChar = self.arguments[index]
            if currentChar[0] == '(':
                valueAndIndex = self.recursion(index)
                values.append(valueAndIndex[0])
                index = valueAndIndex[1]
            else:
                if 48 <= ord(currentChar) <= 57:
                    currentInteger = currentInteger * 10 + int(currentChar)
                elif currentChar == ' ' and self.arguments[index-1] != ')':
                    values.append(int(currentInteger))
                    currentInteger = 0
                index += 1

        if self.arguments[index-1] != ')':
            values.append(currentInteger)
        return self.operation(operator, values), index + 1


    # - Parameters:
    #   - string operator: type of operator in string format
    #   - list[int] values: list containing values to be evaluated with input operator
    # - Return value:
    #   - int: evaluated value based on input operator and values
    def operation(self, operator, values):

        try:
            return getattr(Solution, operator)(values)
        except:
            print("Exception occurred: Invalid Operator")


    # - Parameters:
    #   - list[int] values: list containing values to be multiplied together
    # - Return value:
    #   - int: evaluated value based on input values
    def multiply(values):

        ans = 1
        for value in values:
            if value == 0:
                return 0
            ans *= value
        return ans


    # - Parameters:
    #   - list[int] values: list containing values to be added together
    # - Return value:
    #   - int: evaluated value based on input values
    def add(values):

        ans = 0
        for value in values:
            ans += value
        return ans


    # - Parameters:
    #   - list[int] values: list containing values to be exponentiated together
    # - Return value:
    #   - int: evaluated value based on input values
    def exponent(values):

        ans = values[0]
        for value in range(1, len(values)):
            ans = math.pow(ans, values[value])
        return int(ans)


# Execution code
Solution().parse()



