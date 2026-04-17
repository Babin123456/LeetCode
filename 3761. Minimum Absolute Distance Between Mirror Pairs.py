class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(x):
            return int(str(x)[::-1])
        
        mp = {}  # reversed number -> index
        ans = float('inf')
        
        for i, num in enumerate(nums):
            
            # If current number matches reversed of some previous
            if num in mp:
                ans = min(ans, i - mp[num])
            
            # Store reverse of current number
            rev = reverse_num(num)
            mp[rev] = i
        
        return ans if ans != float('inf') else -1
