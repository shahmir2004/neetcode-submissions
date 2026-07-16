class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table={}
        for eachNumber in nums:
            frequency_table[eachNumber]=frequency_table.get(eachNumber,0)+1

        arr=[]

        for eachNumber,cnt in frequency_table.items():
            arr.append([cnt,eachNumber])
        arr.sort()
        
        result=[]

        while len(result)<k:
            result.append(arr.pop()[1])
        return result

