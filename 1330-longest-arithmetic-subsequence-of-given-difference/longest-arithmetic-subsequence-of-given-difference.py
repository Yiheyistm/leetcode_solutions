class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        pos = defaultdict(int)
        max_seq = 1
        for cur_num in reversed(arr):
            nxt_num = cur_num + difference
            if nxt_num in pos:
                pos[cur_num] = max(pos[cur_num], pos[nxt_num] + 1)
            else: 
                pos[cur_num] = 1
            max_seq = max(max_seq, pos[cur_num])
        return max_seq



        