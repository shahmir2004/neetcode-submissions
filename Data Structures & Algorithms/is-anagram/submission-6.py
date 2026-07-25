class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seenS={}
        seenT={}
        for char in s:
            
                seenS[char]=1+seenS.get(char,0)
        for char in t:
            
                seenT[char]=1+seenT.get(char,0)
        return seenT==seenS
        
        

