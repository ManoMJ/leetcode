class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
        cnt = sum(1 for i in range(k) if s[i] in vowels)

        answer = cnt
        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i-k] in vowels:
                cnt -= 1
            answer = max(cnt, answer)
        
        return answer

