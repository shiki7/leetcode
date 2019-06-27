class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq_list = []
        length = 0
        for num in nums:
            if num not in uniq_list:
                uniq_list.append(num)
                length += 1
        for i, value in enumerate(uniq_list):
            nums[i] = value
        return length
