# 1431. Kids With the Greatest Number of Candies

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for kid in range(len(candies)):
            candies_compare = candies[kid] + extraCandies
            flag = True
            print("El valor que se va a comparar es:", candies[kid])
            for x in candies:
                print("El valor que se va a comparar con el valor anterior es", x)
                if candies_compare < x:
                    flag = False 
            print("El resultado de la flag es:", flag)
            result.append(flag)
        return result
    
    def kidsWithCandiesAISolution(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
    
sol = Solution()

candies = [2,3,5,1,3]
extraCandies = 3

print(sol.kidsWithCandies(candies, extraCandies))