class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        1. All asteroids have the same speed which means asteroid with the same direction never collide
        2. if the first asteroid moves left(-) never collide with an other asteroid which moves to the right (+)
        3. Collision happens when the first moves right and the second moves left
        4. Use stack to track the direction of previous asteroid
        5. The remaining of the stack is the asteroid that are not collide
        '''
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                cl = ast + stack[-1]
                if cl > 0: # the -ve one is explode
                    ast = 0 # break the loop
                elif cl < 0: # the +ve one is explode
                    stack.pop()
                else: # explode each other
                    ast = 0
                    stack.pop()
            if ast:
                stack.append(ast)
        return stack

        