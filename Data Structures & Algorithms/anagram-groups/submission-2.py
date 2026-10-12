class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {} # Sorted Word : list[words]

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord not in anagrams:
                anagrams[sortedWord] = []
            
            anagrams[sortedWord].append(word)
        
        return list(anagrams.values())
        