class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary_num = bin(num)
        binary_num_fixed = binary_num[2:]
        string_num = ""
        for digit in str(binary_num_fixed):
            if digit == "0":
                string_num += "1"
            else:
                string_num += "0"
        return int(string_num, 2)
