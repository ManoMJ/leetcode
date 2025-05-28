class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0

        mx = 0 if nums[0] > nums[1] else 1
        if len(nums)==2:
            return mx
        for i in range(2, len(nums)):
            pp = nums[i-2]
            p = nums[i-1]

            if pp < p and p > nums[i]:
                return i-1
            
            mx = mx if nums[mx] > nums[i] else i

        return mx
              