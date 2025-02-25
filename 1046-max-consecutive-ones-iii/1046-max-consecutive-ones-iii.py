class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flip_cnt = k
        right = 0
        
        while right < len(nums):
            if nums[right]==0 and flip_cnt > 0:
                flip_cnt -= 1
            elif flip_cnt==0:
                break
            right+=1

        answer = right - left
        print(answer)

        while right < len(nums):
            if nums[right] == 0:
                flip_cnt += 1
                
                while left < len(nums) and flip_cnt > 0:
                    if nums[left] == 0:
                        flip_cnt -= 1
                    left += 1
            right += 1
            answer = max(answer, right-left)
        
        return answer