from collections import deque

class Solution :
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        # Step 1 : Fill queues with initial senator indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)


        # Step 2 : Process the voting rounds
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()

            # The senator with the smaller index votes first
            if r_idx < d_idx:
                radiant.append(r_idx + n)  # Re-insert with future index
            else:
                dire.append(d_idx + n)

        # Step 3 : Determine the winner
        return "Radiant" if radiant else "Dire"
