class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair(mid_time):
            t_car = 0
            for r in ranks:
              t_car += int(math.sqrt(mid_time / r)) 
            return t_car >= cars

        max_time = min(ranks) * cars ** 2
        min_time = 0
        while min_time + 1 < max_time:
            mid = (max_time + min_time) // 2 
            if can_repair(mid):
                max_time = mid
            else: min_time = mid
        
        return max_time




        