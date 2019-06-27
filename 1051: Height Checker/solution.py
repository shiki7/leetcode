class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for a, b in zip(heights, sorted_heights):
            if a != b:
                count += 1
        return count
