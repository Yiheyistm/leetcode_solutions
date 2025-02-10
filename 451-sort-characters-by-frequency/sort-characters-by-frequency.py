class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        s = sorted(s, key = lambda x: (-frequency[x], ord(x)))
        return ''.join(s)
        