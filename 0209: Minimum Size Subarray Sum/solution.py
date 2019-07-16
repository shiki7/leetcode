class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        min_len = len(nums) + 1
        total = 0
        for i, num in enumerate(nums):
            total = total + nums[i]
            while total >= s:
                min_len = min(min_len, i-left+1)
                total -= nums[left]
                left += 1
        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len
