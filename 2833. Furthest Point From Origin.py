class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r = 0, 0
        res = 0

        for m in moves:
            if m == 'L': l += 1
            elif m == 'R': r += 1
            else: res += 1

        return res + abs(l - r)
