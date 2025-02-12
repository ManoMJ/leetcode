class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        spointer = 0
        tpointer = 0

        while spointer < len(s) and tpointer < len(t):
            if s[spointer] != t[tpointer]:
                tpointer += 1
            else:
                spointer += 1
                tpointer += 1
        
        return True if spointer==len(s) else False