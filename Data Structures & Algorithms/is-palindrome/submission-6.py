class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = 0
        b = len(s) - 1
        text = s.lower()

        while a < b:
            while a < len(text) and not text[a].isalnum():
                a += 1
            
            while b >= 0 and not text[b].isalnum():
                b -= 1

            if a > b:
                return True
                
            if text[a] != text[b]:
                return False
            
            a += 1
            b -= 1
        
        return True
