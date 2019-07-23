class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse_str = ""
        for char in str(bin(n)[2:].zfill(32)):
            reverse_str = char + reverse_str
        return int(reverse_str, 2)
