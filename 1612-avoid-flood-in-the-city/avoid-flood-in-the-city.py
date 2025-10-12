class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        full_lakes = {}
        prev_zero = []
        for i in range(len(rains)):
            lake = rains[i]
            if lake == 0:
                prev_zero.append(i)
                continue

            if lake in full_lakes:
                prev_idx = full_lakes[lake]
                target_zero_idx = bisect_right(prev_zero, prev_idx)
                
                if target_zero_idx == len(prev_zero): 
                    return []
                nearest_zero_idx= prev_zero.pop(target_zero_idx)
                ans[nearest_zero_idx] = lake

            full_lakes[lake] = i
            ans[i] = -1

        return ans


        