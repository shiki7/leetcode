class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s):
            total += pow(26, (len(s)-i-1))*(ord(char)-ord('A')+1)
        return total
