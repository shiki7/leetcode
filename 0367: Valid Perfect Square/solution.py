class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num) % 1 == 0.0
