class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        sample = "123456789"
        result = []
        
        low_len = len(str(low))
        high_len = len(str(high))
        
        for length in range(low_len, high_len + 1):
            for start in range(10 - length):
                num = int(sample[start:start + length])
                
                if low <= num <= high:
                    result.append(num)
                    
        return result