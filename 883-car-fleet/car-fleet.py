class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
1, Since no car pass the one which near to the target i.e sorting based on position
2, if the destination time of the previous car less than or equal to the next car which mean the are fleet(catch up) and considered as a single car with speed of the smallest (the one near to the target)
3, In order to track the destination time we use stack

        '''
        pairs = zip(position, speed)
        stack = [] # for track car fleet
        
        for p, s in sorted(pairs)[::-1]:
            dest_time = (target - p) / s
            if not stack:
                stack.append(dest_time)
            elif dest_time > stack[-1]:
                stack.append(dest_time)
        return len(stack)
            
