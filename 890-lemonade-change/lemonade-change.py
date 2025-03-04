class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_map = {
            5:0,
            10:0,
            20:0
        }
        for b in bills:
            if b == 10:
                if bill_map[5] > 0:
                    bill_map[5] -= 1
                    bill_map[10] += 1
                else: return False
                
            elif b == 20:
                if bill_map[10] >= 1 and bill_map[5] >= 1:
                    bill_map[5] -= 1
                    bill_map[10] -= 1
                elif bill_map[5] > 2:
                    bill_map[5] -= 3
                else: return False

            else: bill_map[5] += 1
        return True

        