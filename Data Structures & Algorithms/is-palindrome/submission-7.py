class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = 0
        b = len(s) - 1

        while a < b:
            while a < len(s) and not s[a].isalnum():
                a += 1
            
            while b >= 0 and not s[b].isalnum():
                b -= 1

            if a > b:
                return True
                
            if s[a].lower() != s[b].lower():
                return False
            
            a += 1
            b -= 1
        
        return True
