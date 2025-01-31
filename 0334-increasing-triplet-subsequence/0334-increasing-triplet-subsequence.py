class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        second = float('inf')

        for i in range(1, len(nums)):
            if nums[i] < first:
                first = nums[i]
            elif first < nums[i] < second:
                second = nums[i]
            elif nums[i] > second:
                return True
        return False