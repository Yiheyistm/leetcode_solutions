class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse = True)
        n = len(costs)
        min_sum = 0
        a = n // 2
        b = n // 2
        i = 0
        for l, r in costs:
            i += 1
            if a and l < r:
                min_sum += l
                a -= 1
            elif b and r <= l:
                min_sum += r
                b -= 1
            if not a or  not b: break
        while a:
            min_sum += costs[i][0]
            i += 1
            a -= 1

        while b:
            min_sum += costs[i][1]
            i += 1
            b -= 1
        return min_sum
        
                
        