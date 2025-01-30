class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        hasZero = False
        numZero = 0
        for i in nums:
            if i == 0:
                numZero += 1
                hasZero = True
            else:
                mult *= i
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0 and not hasZero:
                result[i] = mult // nums[i]
            if nums[i] == 0 and hasZero:
                result[i] = mult
            if numZero > 1:
                result[i] = 0
                    
        return result

