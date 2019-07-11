import functools
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        
        deck_counter = collections.Counter(deck)
        count_list = list(deck_counter.values())
        min_count = min(count_list)
        if min_count < 2:
            return False
        # 最大公約数
        if functools.reduce(math.gcd, count_list) == 1:
            return False
        return True
