class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spointer = 0
        tpointer = 0

        while spointer < len(s) and tpointer < len(t):
            if s[spointer] == t[tpointer]:
                spointer += 1
                tpointer += 1
            else:
                tpointer += 1
        if spointer == len(s):
            return True
        else:
            return False