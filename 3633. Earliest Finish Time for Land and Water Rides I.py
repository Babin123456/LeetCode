class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        min_finish_time = float('inf')
        
        for i in range(n):
            for j in range(m):
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(land_finish, waterStartTime[j])
                total_time_1 = water_start + waterDuration[j]
                
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(water_finish, landStartTime[i])
                total_time_2 = land_start + landDuration[i]
                
                min_finish_time = min(min_finish_time, total_time_1, total_time_2)
                
        return min_finish_time
