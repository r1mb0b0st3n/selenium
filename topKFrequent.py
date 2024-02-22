from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        returnedList = []
        for x in Counter(nums).most_common(k):
            returnedList.append(x[0])
        return returnedList

        
    
# sol1 = Solution()
# print(sol1.topKFrequent([1,1,1,2,2,3],2))