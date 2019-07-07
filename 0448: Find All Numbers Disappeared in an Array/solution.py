class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # setオブジェクトは要素の引き算ができる(愚直にやろうとするとtimeoutする)
        return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))
