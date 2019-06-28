class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        val = 1
        for i in range(0, 100000):
            if num == val:
                return True
            if num < val:
                return False
            val *= 4
