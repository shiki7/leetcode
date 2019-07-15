class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for x in arr2:
            for i in range(arr1.count(x)):
                ans += [x]
        arr_sorted = sorted(list(set(arr1) - set(arr2)))
        for x in arr_sorted:
            for i in range(arr1.count(x)):
                ans += [x]
        return ans
