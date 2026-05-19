class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        p1, p2 = len(nums1), len(nums2)
        
        while i < p1 and j < p2:
            if nums1[i] == nums2[j]:
                return nums1[i] 
            elif nums1[i] < nums2[j]:
                i += 1  
            else:
                j += 1  
                
        return -1  