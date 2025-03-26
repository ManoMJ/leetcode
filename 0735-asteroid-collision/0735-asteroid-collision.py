class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        # Process the current asteroid
        for i in range(len(asteroids)):
            while  asteroids[i] < 0 and stack and stack[-1] > 0:
                # Case 1 : stack[-1] explodes:
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                    continue

                # Case 2 : Both explode
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                break

            else:
                stack.append(asteroids[i])
            
        return stack