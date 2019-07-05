class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num > 0:
            return hex(num).lstrip('0x')
        elif num < 0:
            return '{:02x}'.format(num & 0xffffffff)
