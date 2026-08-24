class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        sum_diff = 0
        q_diff = 0
        
        for i, ch in enumerate(num):
            sign = 1 if i < n // 2 else -1
            if ch == '?':
                q_diff += sign
            else:
                sum_diff += sign * int(ch)
                
        if q_diff % 2 != 0:
            return True
            

        return sum_diff * 2 + q_diff * 9 != 0