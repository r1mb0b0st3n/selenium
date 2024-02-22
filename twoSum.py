
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """for i in range(0,nums.__len__()):
            if (nums.__len__()-1) != i and returnnedList.__len__() == 0:
                if i<nums.__len__()-4 and returnnedList.__len__() == 0:
                    if (nums[i]+nums[i+1])==target:
                        returnnedList.append(i)
                        returnnedList.append(i+1)
                    if (nums[i]+nums[i+2])==target:
                        returnnedList.append(i)
                        returnnedList.append(i+2)
                    if (nums[i]+nums[i+3])==target:
                        returnnedList.append(i)
                        returnnedList.append(i+3)
                    if (nums[i]+nums[i+4])==target:
                        returnnedList.append(i)
                        returnnedList.append(i+4)
                if i<nums.__len__()-3 and returnnedList.__len__() == 0:
                    if (nums[i]+nums[i+1])==target: 
                        returnnedList.append(i)
                        returnnedList.append(i+1)
                    if (nums[i]+nums[i+2])==target:
                        returnnedList.append(i)
                        returnnedList.append(i+2)
                    if (nums[i]+nums[i+3])==target:
                        returnnedList.append(i)
                        returnnedList.append(i+3)
                if i<nums.__len__()-2 and returnnedList.__len__() == 0:
                    if (nums[i]+nums[i+1])==target:
                        returnnedList.append(i)
                        returnnedList.append(i+1)
                    if (nums[i]+nums[i+2])==target:
                        returnnedList.append(i)
                        returnnedList.append(i+2)
                if (nums[i]+nums[i+1])==target and returnnedList.__len__() == 0:
                    returnnedList.append(i)
                    returnnedList.append(i+1)
        return returnnedList   """
        returnedList = []
        for i in range(nums.__len__()-1):
            for x in range(i+1,nums.__len__()):
                if nums[i] + nums[x] == target and returnedList.__len__() == 0:
                    returnedList.append(i)
                    returnedList.append(x)
        return returnedList                   


# sol1 = Solution()
# print(sol1.twoSum([2,7,11,15],9))