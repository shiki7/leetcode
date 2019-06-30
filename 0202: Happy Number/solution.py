class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            sum = 0
            for i in str(n):
                sum += int(i) * int(i)
            n = sum
            if sum == 1:
                return True
            if sum == 4:
                return False
