import math

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        def is_prime(n):
            if n == 1: return False
            for k in range(2, int(math.sqrt(n)) + 1):
                if n % k == 0:
                    return False
            return True
            
        count = 0
        for i in range(L,R+1):
            bit = 0
            for char in str(bin(i)[2:]):
                if char == "1":
                    bit += 1
            if is_prime(bit):
                count += 1
        return count
