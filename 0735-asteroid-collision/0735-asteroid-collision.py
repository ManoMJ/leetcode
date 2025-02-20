class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # Process the current asteroid
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack[-1]

                # Case 1 : stack[-1] explodes
                if abs(top) < abs(asteroid):
                    stack.pop()
                    continue
                
                # Case 2 : Both explode
                if abs(top) == abs(asteroid):
                    stack.pop()

                # Case 3 : asteroid explods (do not add it to the stack)
                break
            else:
                # If no collision occurred, pusth the asteroid
                stack.append(asteroid)
            
        return stack