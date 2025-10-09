class Solution:
    def isHappy(self, n: int) -> bool:
        st = {n}
        while True:
            new_num = 0
            for ch in str(n):
                new_num += int(ch)**2
            if new_num == 1:
                return True
            if new_num in st:
                return False
            n = new_num
            st.add(n)

        