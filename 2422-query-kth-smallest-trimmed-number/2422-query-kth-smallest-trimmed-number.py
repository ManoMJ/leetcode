from collections import defaultdict

class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        output = []
        n = len(nums)
        num_length = len(nums[0])
        trimmed = defaultdict(list)
        for i, num in enumerate(nums):
            for j in range(1, num_length+1): 
                trimmed[j].append( ( int(num[-j:]), i) )

        for k in trimmed.keys():
            trimmed[k].sort(key= lambda x : x[0])

        print()
        for k, trim_length in queries:
            output.append(trimmed[trim_length][k-1][1])    
        return output
        
        