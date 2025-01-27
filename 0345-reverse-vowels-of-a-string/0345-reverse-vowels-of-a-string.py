class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        vowelary = []
        for ch in s:
            if ch in vowels:
                vowelary.append(ch)
        
        result = []

        for ch in s:
            if ch in vowels:
                result.append(vowelary.pop())
            elif ch not in vowels:
                result.append(ch)
        
        print(result)
        return "".join(result)