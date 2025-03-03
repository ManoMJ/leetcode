class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 0
        cnt = 0
        prev_zero = -1
        zero_cnt = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                cnt = right - prev_zero - 1
                prev_zero = right
            else:
                cnt += 1
            answer = max(cnt, answer)

        if prev_zero < 0:
            answer -= 1

        return answer

