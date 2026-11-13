from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
 
        dq = deque()
        cost = 0
        ans = 0
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            x = nums[l]
            cnt = 1
            
            while dq and dq[-1][0] <= x:
                val, c = dq.pop()
                cost += (x - val) * c
                cnt += c
            dq.append([x, cnt])
            
            while cost > k:
                val, c = dq[0]
                cost -= (val - nums[r])
                if c == 1:
                    dq.popleft()
                else:
                    dq[0][1] -= 1
                r -= 1
                
            ans += (r - l + 1)
            
        return ans