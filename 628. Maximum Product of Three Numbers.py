class Solution:

  def maximumProduct(self, nums: list[int]) -> int:
    nums.sort()
    return max(
        nums[-1] * nums[-2] * nums[-3],  # 3 largest elements
        nums[0] * nums[1] * nums[-1],  # 2 smallest elements * largest element
    )