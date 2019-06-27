class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = str(bin(x)[2:])
        y_bin = str(bin(y)[2:])
        if len(x_bin) < len(y_bin):
            x_bin = "0" * (len(y_bin) - len(x_bin) ) + x_bin
        elif len(x_bin) > len(y_bin):
            y_bin = "0" * (len(x_bin) - len(y_bin) ) + y_bin
        count = 0
        for i in range(0, len(x_bin)):
            if x_bin[i] != y_bin[i]:
                count += 1
        return count
