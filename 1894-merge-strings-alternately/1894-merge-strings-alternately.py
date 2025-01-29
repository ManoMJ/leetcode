class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i , j = 0, 0
        result = ''

        while i < n and j < m:
            result += (word1[i] + word2[j])
            i += 1
            j += 1
        while i < n:
            result += word1[i]
            i += 1
        while j < m:
            result += word2[j]
            j += 1
        return result  