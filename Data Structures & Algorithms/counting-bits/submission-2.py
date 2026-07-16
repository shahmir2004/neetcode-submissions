class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for num in range(n+1):
            numberCount=0
            for i in range(32):
                if(1<<i)&num:
                    numberCount=numberCount+1
            result.append(numberCount)
        return result