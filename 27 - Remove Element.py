from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    # def removeElement(self, nums: List[int], val: int) -> int:
    #     last = len(nums) - 1
    #     k = 0
    #     for i in range(len(nums) // 2):
    #         if nums[i] == val:
    #             if nums[last] == val:
    #                 last -= 1

    #             nums[i], nums[last] = nums[last], nums[i]
    #             k += 1

    #     return nums, k