class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            # Left
            if s[:-1] == s[-2::-1]:
                return True
            # Right
            elif s[1:] == s[:0:-1]:
                return True
            else:
                return False

        l, r = 0, len(s) - 1
        del_count = 0
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s[l:r+1])
        return True

            
            

        
        
        