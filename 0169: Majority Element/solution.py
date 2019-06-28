class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num in count_dict.keys():
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        return max(count_dict, key=count_dict.get)
