class Solution:
    def equalFrequency(self, word: str) -> bool:
        cntr = Counter(Counter(word).values())
        max_freq_val,max_freq = cntr.most_common()[0]
        min_freq_val,min_freq = cntr.most_common()[-1]
        if (len(cntr) == 1 and max(cntr) > 1 and max_freq > 1) or len(cntr) > 2:
            return False
        elif len(cntr) == 1 and (max(cntr) == 1 or max_freq == 1):
            return True
        elif len(cntr) == 2 and min_freq == 1:
            if cntr.get(1, 0) == 1:
                return True
            elif abs(max_freq_val - min_freq_val) ==  1 and max_freq == min_freq:
                return True
            elif max_freq_val + 1 == min_freq_val:
                return True
            else:
                return False
        else: return False
            



        