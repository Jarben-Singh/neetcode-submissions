class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashMap = {}

        for number in nums:
            if number in hashMap:
                return True
            
            hashMap[number] = 1
        
        return False
        