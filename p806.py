class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        MAX_LENGTH = 100
        sum_length = 0
        line = 1
        for char in S:
            sum_length += widths[ord(char)-97]
            if sum_length > MAX_LENGTH:
                line += 1
                sum_length = widths[ord(char)-97]
            elif sum_length == MAX_LENGTH:
                line += 1
                sum_length = 0
                
        return [line, sum_length]
