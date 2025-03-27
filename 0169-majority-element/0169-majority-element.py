from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()  # Sorting the array
        
        return nums[n // 2] 