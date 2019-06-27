class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic.keys():
                dic[num] += 1 
            else:
                dic[num] = 1
        for key, value in dic.items():
            if value == 1:
                return key
