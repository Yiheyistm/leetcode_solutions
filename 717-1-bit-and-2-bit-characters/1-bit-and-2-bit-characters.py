class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                if i + 2 >= len(bits):
                    return False
                i += 2
            else:
                i += 1
        return True


        