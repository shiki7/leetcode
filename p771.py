class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum = 0
        for char_J in J:
            for char_S in S:
                if char_J == char_S:
                    sum += 1
        return sum
        
