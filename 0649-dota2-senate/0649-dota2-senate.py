from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i in range(n):
            if senate[i] == 'D':
                dire.append(i)
            else:
                radiant.append(i)
        
        while radiant and dire:
           
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(n)
            else:
                dire.append(n)
            n += 1
        
        return "Radiant" if radiant else "Dire"
