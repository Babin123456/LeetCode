class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        maxDist = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                maxDist = max(maxDist, j - i)
                j += 1
            else:
                i += 1

        return maxDist