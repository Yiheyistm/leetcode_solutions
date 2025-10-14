class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(len(s)+1): # for odd palindrome
                if i - j < 0 or i + j >= len(s) or s[i-j] != s[i + j]:
                    odd_sub = s[i-j+1:i+j]
                    if len(odd_sub) > len(longest):
                        longest = odd_sub
                    break

            for j in range(len(s)): # for even palindrome
                if i - j < 0 or i + j+ 1 >= len(s) or s[i-j] != s[i + j+1]:
                    even_sub = s[i-j+1:i+j + 1]
                    if len(even_sub) > len(longest):
                        longest = even_sub
                    break

        return longest


        