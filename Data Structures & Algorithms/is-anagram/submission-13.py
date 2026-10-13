class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}  # character : times repeated

        if len(s) != len(t):
            return False

        for c in s:
            if c in hashMap:
                hashMap[c] += 1
            else:
                hashMap[c] = 1
        
        for c in t:
            if c in hashMap:
                hashMap[c] -= 1
            else:
                return False
        
        for c in t:
            if hashMap[c] != 0:
                return False
        
        return True