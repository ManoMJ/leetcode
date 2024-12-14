class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        results = []

        def backtrack(combinations, i):
            if len(combinations) == len(digits):
                results.append("".join(combinations))
                return
            
            for s in phone[digits[i]]:
                combinations.append(s)
                backtrack(combinations, i+1)
                combinations.pop()
        
        backtrack([], 0)
        return results