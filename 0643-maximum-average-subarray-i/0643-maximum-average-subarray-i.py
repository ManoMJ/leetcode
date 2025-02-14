class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subsum = 0
        for i in range(k):
            subsum += nums[i]

        answer = subsum

        for i in range(k, len(nums)):
            subsum -= nums[i-k]
            subsum += nums[i]
            answer = max(subsum, answer)
        
        return answer / k
