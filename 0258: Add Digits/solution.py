class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            sum = 0
            for digit in str(num):
                sum += int(digit)
            if sum / 10 < 1:
                return sum
            num = sum
