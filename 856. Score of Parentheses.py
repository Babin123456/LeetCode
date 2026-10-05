class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Base score level
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                inner_score = stack.pop()
                stack[-1] += max(2 * inner_score, 1)
                
        return stack[0]