from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def get_min_time(start1: List[int], dur1: List[int], start2: List[int], dur2: List[int]) -> int:
            rides1 = sorted(zip(start1, dur1))
            rides2 = sorted(zip(start2, dur2))
            
            n2 = len(rides2)
            
            suffix_min_finish = [0] * (n2 + 1)
            suffix_min_finish[n2] = float('inf')
            for i in range(n2 - 1, -1, -1):
                suffix_min_finish[i] = min(suffix_min_finish[i + 1], rides2[i][0] + rides2[i][1])
            
            ans = float('inf')
            p2 = 0
            min_dur2 = float('inf')  
            
            for s1, d1 in rides1:
                f1 = s1 + d1
                
                while p2 < n2 and rides2[p2][0] <= f1:
                    min_dur2 = min(min_dur2, rides2[p2][1])
                    p2 += 1
                
                if min_dur2 != float('inf'):
                    ans = min(ans, f1 + min_dur2)
                
                if p2 < n2:
                    ans = min(ans, suffix_min_finish[p2])
                    
            return ans

        order1 = get_min_time(landStartTime, landDuration, waterStartTime, waterDuration)
        order2 = get_min_time(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(order1, order2)
