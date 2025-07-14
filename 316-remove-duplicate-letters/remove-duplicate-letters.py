class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        st = set()
        for ch in s:
            while stack and ord(stack[-1]) > ord(ch) and  freq[stack[-1]] and ch not in st:
                c = stack.pop()
                st.remove(c)
            if ch not in st:
                stack.append(ch)
                st.add(ch)
            freq[ch] -= 1
        return ''.join(stack)


        