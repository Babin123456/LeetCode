class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > num * 9:
            return ""
            
        digits = []
        rem_sum = sum
        rem_num = num
        
        for i in range(num):
            for d in range(9, -1, -1):
                if rem_sum - d <= (rem_num - 1) * 9 and rem_sum - d >= 0:
                    digits.append(str(d))
                    rem_sum -= d
                    rem_num -= 1
                    break
                    
        return "".join(digits)