class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num + 1):
            result += [bin(i)[2:].count("1")]
        return result
