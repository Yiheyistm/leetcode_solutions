class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        '''
        mn_time = the required time
        mx = find the the optimal max time that the best mechanics spent to repair all cars by his own
        so it is obvious that mn_time <= mx  if his fellow mechanis help him
        we can find the mid time and calc the no of cars that cleaned at that time
        if numbers of cars less than the total car implies that all cars are not repair in the expexted mid time else numbers of cars greater or equal to total car means they can repair all cars below or at mid times
        '''
        max_time = min(ranks) * cars ** 2 # the optimal max time 
        min_time = 1
        while min_time < max_time:
            # r* n**2 = m
            # n = math.sqrt(m/r)
            mid = (max_time + min_time) // 2 # does all cars are repair in the mid time 
            total_cars = 0 # count the no cars do repair in the mid time
            for r in ranks: # check does mechanics finish repair all cars
                total_cars += int(math.sqrt(mid / r))
                if total_cars >= cars: break
            if total_cars >= cars:
                max_time = mid
            else: min_time = mid + 1
        return min_time




        