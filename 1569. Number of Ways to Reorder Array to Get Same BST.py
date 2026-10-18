import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            ways_comb = math.comb(len(left) + len(right), len(left))
            
            return (ways_comb * helper(left) * helper(right)) % MOD
            
        return (helper(nums) - 1 + MOD) % MOD
