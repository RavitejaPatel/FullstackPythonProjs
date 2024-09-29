from typing import List


class Solution:

    def printNums(self, nums: List[int]):
        res=''
        for val in nums:
            res += " " + str(val)
        print(res)

    def removeDuplicates(self, nums: List[int]) -> int:
        p1=0
        p2=1
        while p1 <= p2 and p2 < len(nums):
            if nums[p1]!=nums[p2]:
                nums[p1+1]=nums[p2]
                p1+=1
            p2+=1
        self.printNums(nums)
        return p1+1



nums=[1,1,2,2,3]
print(f"Num of Uniques exists {Solution().removeDuplicates(nums=nums)}")