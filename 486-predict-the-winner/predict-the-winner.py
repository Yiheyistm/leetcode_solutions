class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def option(l, r, isPlayer1):
            if l > r:
                return 0
      
            if isPlayer1:
                left_option = nums[l] + option(l + 1, r, False)
                right_option = nums[r] + option(l, r - 1, False)
                return max(left_option, right_option)
            else:
                option_left = option(l + 1, r, True)
                option_right = option(l, r - 1, True)
                return min(option_left, option_right)
                
        total = sum(nums)
        player1 =  option(0, len(nums) -1, True)
        player2 = total - player1
        return player1 >= player2
                    


        