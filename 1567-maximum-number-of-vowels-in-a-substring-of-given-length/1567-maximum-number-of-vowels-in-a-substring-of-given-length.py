class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(list("aeiouAEIOU"))
        
        vc = 0
        for i in range(k):
            if s[i] in vowels:
                vc += 1
        answer = vc
        
        for i in range(k, len(s)):
            print(vc)
            if s[i-k] in vowels:
                vc -= 1
            if s[i] in vowels:
                vc += 1
            if vc > answer:
                answer = vc
        
        return answer
