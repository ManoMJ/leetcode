class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bigger = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= bigger:
                result.append(True)
            else:
                result.append(False)
        
        return result
        