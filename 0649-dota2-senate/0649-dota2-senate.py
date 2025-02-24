from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        n = len(senate)
    
        radient_cnt = senate.count("R")
        dire_cnt = senate.count("D")
        senate = deque(map(str, senate))
        radient_pointer, dire_pointer = 0, 0

        pointer = 0
        
        print("radient : ", radient_cnt, "dire : ", dire_cnt)

        while True:
           

            if radient_cnt == 0:
                return "Dire"
            elif dire_cnt == 0:
                return "Radiant"
            
            if senate[pointer] == 'R':
                radient_pointer = pointer
                dire_pointer = pointer
                while True:
                    if senate[dire_pointer] == 'D':
                        break
                    dire_pointer = (dire_pointer+1)%n
                if dire_pointer < n:
                    senate[dire_pointer] = 'Q'
                    dire_cnt -= 1
            elif senate[pointer] == 'D':
                dire_pointer = pointer
                radient_pointer = pointer
                while radient_pointer < n:
                    if senate[radient_pointer] == 'R':
                        break
                    radient_pointer = (radient_pointer+1)%n
                if radient_pointer < n:
                    senate[radient_pointer] = 'Q'
                    radient_cnt -= 1
            
            pointer = (pointer+1)%n

        
            
        
