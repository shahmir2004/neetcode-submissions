class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        arr=[]
        for number,count in count.items():
            arr.append([count,number])
        arr.sort()
        result=[]
        for i in range(k):
            result.append(arr.pop()[1])
        return result



