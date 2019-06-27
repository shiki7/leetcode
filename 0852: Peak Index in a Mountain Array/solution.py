class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max = 0
        peak_index = 0
        for i, number in enumerate(A):
            if number > max:
                max = number
                peak_index = i
        return peak_index
