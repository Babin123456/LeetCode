class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_count, close_count, current_str):
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
            
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")

        backtrack(0, 0, "")
        return res
