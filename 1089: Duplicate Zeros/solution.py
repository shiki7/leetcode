class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        shift = 0
        for i, x in enumerate(arr.copy()):
            if x == 0:
                arr.insert(i+shift, 0)
                arr.pop()
                shift += 1
