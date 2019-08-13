# DFS + memo
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        def DFS(nums, i, summary):
            if i == len(nums):
                if summary == S:
                    memo[(i, summary)] = 1
                else:
                    memo[(i, summary)] = 0
            if (i, summary) not in memo:
                memo[(i, summary)] = DFS(nums, i+1, summary+nums[i]) + DFS(nums, i+1, summary-nums[i])
            return memo[(i, summary)]
        DFS(nums, 0, 0)
        return memo[(0,0)]
