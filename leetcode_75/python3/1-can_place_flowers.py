from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # How to solve this.
        # Check if there are spots for a flower, there needs to be three spots.
        flower_amount = 0
        flowerbed_temp = flowerbed
        for flower in range(len(flowerbed)):
            # Must check if a flower can be in this position.
            if flowerbed[flower] == 0 and flower + 1 <= len(flowerbed) - 1 and flowerbed[flower+1] == 0 and flowerbed[flower-1] == 0 and flower - 1 >= 0:
                flower_amount += 1
                flowerbed_temp[flower] = 1
            elif flower == 0 and flower + 1 <= len(flowerbed)- 1 and flowerbed[flower] == 0 and flowerbed[flower+1] == 0:
                flower_amount += 1
                flowerbed_temp[flower] = 1
            elif flower == len(flowerbed) - 1 and flowerbed[flower] == 0 and flowerbed[flower-1] == 0 and flower - 1 >= 0:
                flower_amount += 1
                flowerbed_temp[flower] = 1
            elif flowerbed == [0]:
                flower_amount += 1
            elif flowerbed == 1 and flowerbed[flower + 1] == 0 and flower + 1 != len(flowerbed) + 1:
                continue
        print(flower_amount)
        if flower_amount >= n:
            return True
        else: 
            return False
    def canPlaceFlowersOptimized(self, flowerbed: List[int], n: int) -> bool:
        flower_amount = 0
        
        for flower in range(len(flowerbed)):
            if flowerbed[flower] == 0:
                left_empty = (flower == 0 or flowerbed[flower-1] == 0)
                right_empty = (flower == len(flowerbed) - 1 or flowerbed[flower+1] == 0)

                if left_empty and right_empty:
                    flowerbed[flower] = 1
                    flower_amount += 1
                    if flower_amount >= n:
                        return True
        return flower_amount >= n
sol = Solution()

flowerbed = [1,0,1,0,1,0,1]
n = 0

print(sol.canPlaceFlowersOptimized(flowerbed, n))