class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(0, len(flowerbed)):
            if not flowerbed[i]:
                if i==0 and len(flowerbed) > 1 and not flowerbed[i+1]:
                    flowerbed[i]=1
                    n = n-1
                elif i==len(flowerbed)-1 and not flowerbed[i-1]:
                    flowerbed[i]=1
                    n = n-1
                elif not i==len(flowerbed)-1 and not flowerbed[i+1] and not flowerbed[i-1]:
                    flowerbed[i]=1
                    n = n-1

        if n > 0:
            return False
        else:
            return True       