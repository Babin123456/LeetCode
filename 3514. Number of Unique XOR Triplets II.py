class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        U = set(nums)
        
        P = {a ^ b for a in U for b in U}
        
        triplets = {p ^ c for p in P for c in U}
        
        return len(triplets)
