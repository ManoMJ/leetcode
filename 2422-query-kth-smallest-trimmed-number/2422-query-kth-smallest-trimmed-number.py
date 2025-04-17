from collections import defaultdict
# 1318 ms
class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        # Collect Only the needed trim lengths from the queries
        needed_trims = {trim for _, trim in queries}

        # Precompute a dictionary for these trim lengths using lexicographic order.
        trimmed = {}
        for t in needed_trims:
            # Create a list of (trimmed_value, original_index) tuples.
            # Since all trimmed strings are of equal length, lexicographic order works.
            trimmed[t] = sorted((num[-t:], i) for i, num in enumerate(nums))

        # For each query, find the k-th smallest trimed number's original index.
        result = []
        for k, t in queries:
            result.append(trimmed[t][k-1][1])

        return result
        
        