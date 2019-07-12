class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        l = 0 
        r = len(height) - 1
        while l < r: 
            maxA = max(min(height[l], height[r]) * (r - l), maxA)
            if height[l] < height[r]: 
                l += 1 
            else: 
                r -= 1
        return maxA