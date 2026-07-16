class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1={}
        seen2={}
        if (len(s)!=len(t)):
            return False
        for i in range(len(s)):
            seen1[s[i]]=1+seen1.get(s[i],0)
        for i in range(len(t)):
            seen2[t[i]]=1+seen2.get(t[i],0)
        return seen1==seen2

