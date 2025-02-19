class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) < 2:
            return asteroids

        asteroids.reverse()
        stack = [asteroids.pop()]
        
        while asteroids:
            a1 = asteroids.pop()
            if a1 < 0 and stack and stack[-1] > 0:
                flag = False
                while a1 < 0 and stack and stack[-1] > 0:
                    a2 = stack[-1]
                    if abs(a1) > abs(a2):
                        stack.pop()
                        flag  = True
                    elif abs(a1) == abs(a2) :
                        stack.pop()
                        a1 = 1
                        flag = False
                    else:
                        a1 = 1
                        flag= False
                if flag:
                    stack.append(a1)
            else:
                stack.append(a1)
        
        print("stack", stack)

        while stack and len(stack)>1 and stack[-2] > 0 and stack[-1] < 0:
            
            a1 = stack.pop()
            a2 = stack.pop()
            print(a1, a2)
            if abs(a1) > abs(a2):
                stack.append(a1)
            elif abs(a1) < abs(a2) :
                stack.append(a2)
                
        return stack
