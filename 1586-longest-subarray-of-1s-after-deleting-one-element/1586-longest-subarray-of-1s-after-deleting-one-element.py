class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0

        zero = -1
        answer = 0
        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                start += 1
            else:
                break
        
        length = 0

        for i in range(start, len(nums)):
            
            if nums[i]==1:
                length += 1
            else:
                if zero > 0:
                    length = i - zero - 1
                zero = i
            answer = max(answer, length)

            print(length)
        return answer if zero > 0 or start > 0 else len(nums)-1

