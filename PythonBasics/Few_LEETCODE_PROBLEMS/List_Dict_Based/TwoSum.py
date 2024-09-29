from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        result = []
        for i, n in enumerate(nums):
            rem = target-n
            if not res.__contains__(rem):
                res[n]=i
            else:
                result.append(res[rem])
                result.append(i)
                # return [res[rem], i]
        return result

def main():
    print("---------------------------TWO SUM LC---------------------------------------")
    nums = [2,7,11,15]
    target=9
    print(type(nums))
    soln=Solution()
    print(soln.twoSum(nums=nums,target=target))

if __name__ == '__main__':
    main()

             

