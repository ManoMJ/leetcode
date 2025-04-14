from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers_dict = defaultdict(int)

        for num in nums:
            numbers_dict[num] += 1
    
        for num in numbers_dict.keys():
            if numbers_dict[num] < 2:
                return num
        