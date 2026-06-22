from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        
        b = counts['b']
        a = counts['a']
        l = counts['l'] // 2
        o = counts['o'] // 2
        n = counts['n']
        
        return min(b, a, l, o, n)
