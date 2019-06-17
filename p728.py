class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for x in range(left, right + 1):
            isSelfDividing = True
            string = str(x)
            for digit_str in string:
                digit = int(digit_str)
                if digit == 0 or x % digit != 0:
                    isSelfDividing = False
                    break
            if isSelfDividing:
                result += [x]
        return result
