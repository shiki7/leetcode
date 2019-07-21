class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        
        out = [nums[0], max(nums[:2])]
        for i in range(2,len(nums)):
            out.append(max(out[-1], out[-2] + nums[i]))
        return out[-1]
