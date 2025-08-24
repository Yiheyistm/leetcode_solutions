class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def bs(ch, max_):
            if ch not in char_dict:
                return -1

            l = -1
            h = len(char_dict[ch]) - 1
            while l + 1 < h:
                mid = (l + h) // 2
                if char_dict[ch][mid] >= max_: h = mid
                else: l = mid
            return char_dict[ch][h]

        cnt = 0
        char_dict = defaultdict(list)
        for i, ch in enumerate(s):
            char_dict[ch].append(i)

        for word in words:
            max_ = 0
            ln = 0
            for ch in word:
                md = bs(ch, max_)
                if md < max_: break
                max_ = md + 1
                ln += 1

            if ln == len(word):
                cnt += 1
        return cnt
            

        

        