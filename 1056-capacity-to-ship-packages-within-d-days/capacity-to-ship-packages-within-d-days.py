class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(capacity):
            nonlocal weights, days
            curr_weight_sum = 0
            day_count = 1
            for w in weights:
                curr_weight_sum += w
                if curr_weight_sum > capacity:
                    day_count += 1
                    curr_weight_sum = 0
                    curr_weight_sum += w
                    if day_count > days:
                        return False
            return True
        
        low, high = max(weights), sum(weights)
        while low <= high:
            mid = (low + high) // 2
            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
        