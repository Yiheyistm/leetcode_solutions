class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        frequency = dict(sorted(frequency.items(), key = lambda freq: (-freq[1],freq[0])))
        
        ans = ''
        for key, value in frequency.items():
            ans += key * value

        return ans
        