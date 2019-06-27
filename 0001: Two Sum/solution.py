class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indexA, a in enumerate(nums):
            for indexB, b in enumerate(nums):
                if indexA >= indexB :
                    continue
                if a + b == target:
                    return [indexA, indexB]
