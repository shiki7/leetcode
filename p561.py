class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        sum = 0
        for i in range(0, len(nums), 2):
            sum += min(nums[i:i+1])
        return sum
