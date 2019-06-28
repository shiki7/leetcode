class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 1
        for i in range(0, 100000):
            if n == num:
                return True
            if n < num:
                return False
            num *= 3
