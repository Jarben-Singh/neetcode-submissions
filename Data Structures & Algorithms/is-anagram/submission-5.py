class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c in map:
                map[c] = map[c] + 1
            else:
                map[c] = 1

        for c in t:
            if c not in map:
                return False

            if c in map:
                map[c] = map[c] - 1

            if map[c] < 0:
                return False
            
        
        return True

