class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString=''
        for c in s:
            if c.isalnum():
                newString=newString+c.lower()
        return "".join(reversed(newString))==newString