class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceMap={}
        for i, n in enumerate(nums):
            difference=target-n
            if difference in differenceMap:
                return [differenceMap[difference],i]
            differenceMap[n]=i
        

