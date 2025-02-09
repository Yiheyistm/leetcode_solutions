class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        min_sum = 0
        rabits_map = {}

        for ans in answers: 
            if ans == 0:
                min_sum += 1
            elif ans in rabits_map and rabits_map[ans] == ans:
                min_sum += ans + 1
                del rabits_map[ans]
            else:
                rabits_map[ans] = rabits_map.get(ans, 0) + 1

        for key in rabits_map:
            min_sum += key + 1
        return min_sum
            



        