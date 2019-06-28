class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_dict = {}
        ans = []
        for num in nums:
            if num in count_dict.keys():
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        for key, value in count_dict.items():
            if value > len(nums) / 3:
                ans += [key]
        return ans
