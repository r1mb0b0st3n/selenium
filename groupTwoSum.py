# Two sum group 
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nDict = dict()
        for i,n in enumerate(numbers):
            result = target-n
            if result in nDict:
                return[nDict[result],i]
            else:
                nDict[n] =i
        return []
        
        
# sol1=Solution()
# print(sol1.twoSum([2,7,11,15],9))