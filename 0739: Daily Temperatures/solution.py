class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)
        for i , temp in enumerate(T):
            while len(stack) > 0 and temp > stack[-1][1]:
                index, t = stack.pop()
                result[index] = i - index
            stack.append((i, temp))
        return result
