class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        str_x_reverse = str_x[::-1]
        if str_x == str_x_reverse:
            return True
        else:
            return False
