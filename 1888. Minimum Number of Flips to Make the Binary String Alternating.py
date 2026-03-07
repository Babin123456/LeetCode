class Solution:
    def minFlips(self, s: str) -> int:
        w = len(s)
        s = s*2
        n = len(s)

        def solve(tar):
            curr = 0
            prev_tar = [0] * n
            for i in range(w):
                if s[i] != tar: curr += 1
                prev_tar[i] = tar
                tar = '1' if tar == '0' else '0'

            res = curr
            for i in range(w, n):
                if s[i - w] != prev_tar[i - w]: curr -= 1
                if s[i] != tar: curr += 1
                res = min(res, curr)
                tar = '1' if tar == '0' else '0'
            return res

        return min(solve('0'), solve('1'))
