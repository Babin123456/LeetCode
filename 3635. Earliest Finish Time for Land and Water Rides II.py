import bisect
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def solve_one_way(start1: List[int], dur1: List[int], start2: List[int], dur2: List[int]) -> int:
            rides2 = sorted(zip(start2, dur2))
            n2 = len(rides2)
            
            if n2 == 0:
                return float('inf')
            
            prefix_min_dur = [0] * n2
            prefix_min_dur[0] = rides2[0][1]
            for i in range(1, n2):
                prefix_min_dur[i] = min(prefix_min_dur[i - 1], rides2[i][1])
                
            suffix_min_finish = [0] * (n2 + 1)
            suffix_min_finish[n2] = float('inf')
            for i in range(n2 - 1, -1, -1):
                suffix_min_finish[i] = min(suffix_min_finish[i + 1], rides2[i][0] + rides2[i][1])
                
            start_times2 = [r[0] for r in rides2]
            best_time = float('inf')
            
            for s1, d1 in zip(start1, dur1):
                f1 = s1 + d1
                
                idx = bisect.bisect_right(start_times2, f1)
                
                if idx > 0:
                    best_time = min(best_time, f1 + prefix_min_dur[idx - 1])
                    
                if idx < n2:
                    best_time = min(best_time, suffix_min_finish[idx])
                    
            return best_time

        ans1 = solve_one_way(landStartTime, landDuration, waterStartTime, waterDuration)
        ans2 = solve_one_way(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(ans1, ans2)
