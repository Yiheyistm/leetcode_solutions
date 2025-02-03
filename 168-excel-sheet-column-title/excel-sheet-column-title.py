class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        reminder = []
        while columnNumber > 0:
            columnNumber -= 1
            reminder.append(columnNumber % 26)
            columnNumber //= 26
        ans = ''
        print(reminder[::-1])
        for i in range(len(reminder)-1, -1 , -1):
            ans += chr(reminder[i] + 65)
        return ans
 

        