class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        y = sorted(costs, key = lambda x: x[0] - x[1])
        total = 0
        for index,value in enumerate(y):
            if index < len(y)//2:
                total += value[0]
            else:
                total += value[1]
        return total
