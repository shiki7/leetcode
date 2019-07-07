from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for k,v in counts.items():
            if v == 1:
                return s.index(k)
        return -1
