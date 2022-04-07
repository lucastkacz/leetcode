from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x**2 for x in nums]

        left, right = 0, len(nums) - 1
        results = []

        while left <= right:
            if nums[left] > nums[right]:
                results.append(nums[left])
                left += 1
            else:
                results.append(nums[right])
                right -= 1

        return results[::-1]