class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y
        count = 0
        while X != Y:
            count += 1
            if Y > X and Y % 2 == 0:
                Y /= 2
            else:
                Y += 1
        return count
