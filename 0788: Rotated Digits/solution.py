class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        total = 0
        dic = {"0":"0", "1":"1","2":"5","5":"2","6":"9","8":"8","9":"6"}
        def rotate(num):
            str_nums = str(num)
            converted_num = ""
            for str_num in str_nums:                
                if not str_num in dic:
                    return False
                else:
                    converted_num += dic[str_num]
            if converted_num != str_nums:
                return True
            else:
                return False
        for num in range(1, N+1):
            if rotate(num):
                total += 1
        return total
