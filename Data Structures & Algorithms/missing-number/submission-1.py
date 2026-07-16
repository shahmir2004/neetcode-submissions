class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        numberNotIncluded=0
        n=len(nums)
        seen={}
        for num in nums:
            if num not in seen:
                seen[num]=True
        for i in range(n+1):            
            if i not in seen:
                numberNotIncluded= i
        return numberNotIncluded




       