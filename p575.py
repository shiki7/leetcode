class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        max_kinds = int (len(candies) / 2)
        uniq_kinds = len(set(candies))
        if uniq_kinds > max_kinds:
            return max_kinds
        else:
            return uniq_kinds
