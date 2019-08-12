class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = nums.count(0)
        count1 = nums.count(1)
        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0+count1):
            nums[i] = 1
        for i in range(count0+count1, len(nums)):
            nums[i] = 2
