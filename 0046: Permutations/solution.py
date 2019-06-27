class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        ans = []
        for i in itertools.permutations(nums):
            ans += [i]
        return ans
