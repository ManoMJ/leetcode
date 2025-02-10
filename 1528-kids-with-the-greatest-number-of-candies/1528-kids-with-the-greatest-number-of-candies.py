class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        big = max(candies)
        result = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= big:
                result[i] = True
        return result