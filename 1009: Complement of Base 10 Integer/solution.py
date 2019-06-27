class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = ""
        for char in str(bin(N)[2:]):
            if char == '0':
                s += '1'
            else:
                s += '0'
        return int(s, 2)
