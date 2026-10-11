class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        a = 0
        b = len(numbers) - 1

        while a < b:
            if numbers[a] + numbers[b] == target:
                return [a + 1, b + 1]
            
            if target > numbers[a] + numbers[b]:
                a += 1
            else:
                b -= 1