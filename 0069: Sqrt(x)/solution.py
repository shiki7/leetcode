
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # linear(timeover)
        # for i in range(1, 10 ** 5):
        #     if x == i ** 2:
        #         return i
        #     elif x < i ** 2:
        #         return i - 1
        
        # newton
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
