class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = 0
        prev = 0
        for n in gain:
            current = prev + n
            prev = current
            answer = max(current, answer)
        return answer