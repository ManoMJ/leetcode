class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        answer = (r - l) * min(height[l], height[r])

        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            answer = max(answer, (r - l) * min(height[l], height[r]))
        
        return answer
            
            
