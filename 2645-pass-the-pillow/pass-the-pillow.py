class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = time // (n - 1) # for n it require n - 1 time
        remain_time = time % (n - 1) # the remian time from the cycle

        if cycle % 2 == 0: # if it is even the direction is to the left else to the right
            return remain_time + 1
        else:
            return n - remain_time


        