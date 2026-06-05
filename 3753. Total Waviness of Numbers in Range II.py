from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def get_waviness_up_to(n_str: str) -> int:
            length = len(n_str)
            
            @lru_cache(None)
            def dp(idx, tight, leading_zero, last, prev):
                if idx == length:
                    return 0
                
                limit = int(n_str[idx]) if tight else 9
                total_waviness = 0
                
                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
                    
                    if leading_zero:
                        if d == 0:
                            total_waviness += dp(idx + 1, new_tight, True, -1, -1)
                        else:
                            total_waviness += dp(idx + 1, new_tight, False, d, -1)
                    else:
                        is_waviness = 0
                        if prev != -1 and last != -1:
                            if prev < last > d:    # Peak
                                is_waviness = 1
                            elif prev > last < d:  # Valley
                                is_waviness = 1
                        
                        
            return dp
            
        def count_and_sum(n_str: str) -> int:
            length = len(n_str)
            
            @lru_cache(None)
            def dp(idx, tight, leading_zero, last, prev):
                if idx == length:
                    return 0, 1  
                limit = int(n_str[idx]) if tight else 9
                ans_waviness = 0
                ans_count = 0
                
                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
                    
                    if leading_zero:
                        if d == 0:
                            w, c = dp(idx + 1, new_tight, True, -1, -1)
                        else:
                            w, c = dp(idx + 1, new_tight, False, d, -1)
                    else:
                        w, c = dp(idx + 1, new_tight, False, d, last)
                        if prev != -1 and last != -1:
                            if (prev < last > d) or (prev > last < d):
                                w += c  
                    ans_waviness += w
                    ans_count += c
                    
                return ans_waviness, ans_count
                
            return dp(0, True, True, -1, -1)[0]

        return count_and_sum(str(num2)) - count_and_sum(str(num1 - 1))
