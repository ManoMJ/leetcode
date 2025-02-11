class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        answer = sum
        print(sum)
        for i in range(k, len(nums)):
            sum -= nums[i-k]
            sum += nums[i]
            print(sum)
            if sum > answer:
                answer = sum
        return answer / k