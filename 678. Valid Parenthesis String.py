class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # Min possible open parentheses
        high = 0  # Max possible open parentheses

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('

            if high < 0:
                return False

            if low < 0:
                low = 0

        return low == 0
