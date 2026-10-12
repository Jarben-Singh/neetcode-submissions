class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        maxArea = 0

        while a < b:
            if min(heights[a], heights[b]) * (b - a) > maxArea:
                maxArea = min(heights[a], heights[b]) * (b - a)
            
            if heights[a] < heights[b]:
                a += 1
            else:
                b -= 1
        
        return maxArea