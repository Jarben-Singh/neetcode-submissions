class Solution:
    def isPalindrome(self, s: str) -> bool:
        sClean = ""

        for c in s:
            if c.isalnum():
                sClean += c
        
        sClean = sClean.lower()

        a = 0
        b = len(sClean) - 1

        while a < b:
            if sClean[a] != sClean[b]:
                return False
            
            a += 1
            b -= 1
        
        return True