class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        answer = 0
        alti = 0
        for g in gain:
            alti += g
            answer = max(alti, answer)
        return answer
        