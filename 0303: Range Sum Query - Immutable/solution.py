class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.sums[i] = total
        
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1]
