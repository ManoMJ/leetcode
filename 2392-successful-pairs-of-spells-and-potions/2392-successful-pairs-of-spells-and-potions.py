from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        res = []
        for spell in spells:
            min_required = (success + spell - 1) // spell  # 올림 처리
            idx = bisect_left(potions, min_required)
            res.append(m - idx)
        return res
