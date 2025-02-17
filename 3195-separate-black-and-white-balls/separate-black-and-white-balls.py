class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        steps = 0
        freq_map = defaultdict(int)
        for r in range(len(s) - 1, -1, -1):
            freq_map[s[r]] += 1
            if s[r] == '1':
                steps += freq_map['0']

        return steps

        