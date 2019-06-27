class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = []
        for index, item in reversed(list(enumerate(nums))):
            if item == val:
                del nums[index]
