class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if str_x[-1] == 0:
            str_x = str_x[:-1]
        if str_x[0] == "-":
            temp = str_x[1:]
            str_x = str_x[0] + temp[::-1]
        else:
            str_x = str_x[::-1]
        int_x = int(str_x)
        if int_x > 2**31 - 1 or int_x < -(2**31):
            return 0
        else:
            return int_x
