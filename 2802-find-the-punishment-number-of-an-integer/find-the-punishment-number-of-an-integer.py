class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s, target, index, current_sum):
            if index == len(s):
                return current_sum == target
            
            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                num = int(substring)
                
                if can_partition(s, target, i, current_sum + num):
                    return True
            
            return False

        punishment = 0
        for i in range(1, n + 1):
            square = i * i
            if can_partition(str(square), i, 0, 0):
                punishment += square
        
        return punishment
        