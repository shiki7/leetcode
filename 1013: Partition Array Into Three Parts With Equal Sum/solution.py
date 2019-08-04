class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        PARTITION_SUM = sum(A)/3
        total = 0
        count = 0
        for num in A:
            total += num
            if total == PARTITION_SUM:
                total = 0
                count += 1
        return count == 3 and total == 0
