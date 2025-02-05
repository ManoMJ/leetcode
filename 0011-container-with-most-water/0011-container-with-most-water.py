class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        h = min(height[r], height[l])
        w = r - l
        e = h * w
        
        while l < r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
            if (r-l) * min(height[r], height[l]) > e:
                e = (r-l) * min(height[r], height[l])

        return e