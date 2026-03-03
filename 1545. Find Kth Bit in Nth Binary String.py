s = '0'
for i in range(19):
    inv = ''
    for c in s: inv += '1' if c == '0' else '0'
    s += '1' + inv[::-1]

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return s[k - 1]
        