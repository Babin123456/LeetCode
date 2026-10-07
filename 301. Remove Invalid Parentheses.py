class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []

        def remove(s, last_i, last_j, open_paren, close_paren):
            count = 0
            for i in range(last_i, len(s)):
                if s[i] == open_paren:
                    count += 1
                if s[i] == close_paren:
                    count -= 1
                if count >= 0:
                    continue

                for j in range(last_j, i + 1):
                    if s[j] == close_paren and (j == last_j or s[j - 1] != close_paren):
                        remove(s[:j] + s[j + 1:], i, j, open_paren, close_paren)
                return

            reversed_s = s[::-1]
            if open_paren == '(':  # Finished left-to-right pass, now do right-to-left
                remove(reversed_s, 0, 0, ')', '(')
            else:
                res.append(reversed_s)

        remove(s, 0, 0, '(', ')')
        return res
