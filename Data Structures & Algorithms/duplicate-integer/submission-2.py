class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberMap = {} # number : count

        for x in nums:
            if x in numberMap:
                return True
            else:
                numberMap[x] = 1
        
        return False