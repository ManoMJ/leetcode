from collections import Counter 

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        answer = 0

        for num in count.keys():
            supplement = k - num
            if supplement == num:
                answer += count[num]//2
            elif supplement in count.keys():
                add = min(count[num], count[supplement])
                answer += add
                count[supplement] -= add
            count[num] = 0
            
        return answer