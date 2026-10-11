class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {} # sorted : list

        for s in strs:
            key = tuple(sorted(s))

            if key not in hashMap:
                hashMap[key] = []
            
            hashMap[key].append(s)
        
        return list(hashMap.values())


        
        