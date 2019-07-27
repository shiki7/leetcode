class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        ans = []
        for freq in counter.most_common(k):
            ans += [freq[0]]
        return ans
