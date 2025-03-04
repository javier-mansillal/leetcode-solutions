# 2161. Partition Array According to Given Pivot
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_than_pivot = []
        bigger_than_pivot = []
        pivot_list = []
        for num in nums:
            if num < pivot:
                smaller_than_pivot.append(num)
            elif num > pivot:
                bigger_than_pivot.append(num)
            elif num == pivot:
                pivot_list.append(num)
        nums = smaller_than_pivot + pivot_list + bigger_than_pivot
        return nums
            


sol = Solution()

nums = [-3,4,3,2]
pivot = 2

print(sol.pivotArray(nums, pivot))