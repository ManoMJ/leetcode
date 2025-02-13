class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums)==0:
            return 0
        answer = 0
        flipped = k
        length = 0
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
            else:
                zeros.append(i)
                if flipped > 0:
                    length += 1
                    flipped -= 1
                else:
                    flipped = 0
                    length = i - zeros[len(zeros)-1-k]
            answer = max(answer, length)
            print(length)
        
        return answer


        