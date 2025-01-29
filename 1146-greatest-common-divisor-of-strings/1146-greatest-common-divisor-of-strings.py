class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ''

        n = len(str1)
        m = len(str2)

        smaller = n if n < m else m
        
        if n == 1 or m ==1:
            return str1[:smaller]
        
        i = 2
        for i in range(smaller, 1, -1):
            if n%i==0 and m%i==0:
                break
        return str1[:i]

