# 2570. Merge Two 2D Arrays by Summing Values
from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result_dict = {}
        result = []
        for x,y in nums1:
            result_dict.update({x: [y]})
        for x,y in nums2:
            if x in result_dict:
                result_dict[x].append(y)
            else:
                result_dict.update({x:[y]})
        for x,y in result_dict.items():
            result.append([x, sum(y)])
        return sorted(result, key=lambda x: x[0])
    
    # The same as mergeArrays but with AI improvements.
    def mergeArraysAIimproved(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result_dict = {}

        # One loop for both arrays.
        for x, y in nums1 + nums2:
            if x in result_dict:
                result_dict[x] += y  # Do a direct sum instead of append + sum
            else:
                result_dict[x] = y

        # Return sorted pairs.
        return sorted(result_dict.items())

sol = Solution()

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

print(sol.mergeArrays(nums1, nums2))
print(sol.mergeArraysAIimproved(nums1, nums2))
