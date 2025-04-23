class Solution:
    def partitionString(self, s: str) -> int:
        mn = 1
        st = set()
        for ch in s:
            if ch not in st: st.add(ch)
            else:
                mn += 1
                st = set(ch)
        return mn
        