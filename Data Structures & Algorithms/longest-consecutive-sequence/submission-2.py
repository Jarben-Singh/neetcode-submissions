class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for key in s:
            if key - 1 not in s:
                n = key
                counter = 1

                while n + 1 in s:
                    counter += 1
                    n += 1
                
                longest = max(counter, longest)
        
        return longest
        
    
            
            
