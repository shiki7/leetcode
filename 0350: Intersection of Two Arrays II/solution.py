class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list_uniq = list(set(nums1) & set(nums2))
        ans = []
        for char in list_uniq:
            for i in range(0, min(nums1.count(char), nums2.count(char))):
                ans += [char]
        return ans
