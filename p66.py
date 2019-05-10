class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ""
        for digit in digits:
            string += str(digit)
        return str(int(string) + 1)
