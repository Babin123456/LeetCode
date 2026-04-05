class Solution:
    def judgeCircle(self, moves: str) -> bool:
        fm = Counter(moves)

        return fm['U'] == fm['D'] and fm['L'] == fm['R']