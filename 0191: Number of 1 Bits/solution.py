class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for char in str(bin(n)[2:]):
            if char == "1":
                total += 1
        return total
