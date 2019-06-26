class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = []
        for num in sorted(deck, reverse=True):
            # 末尾を先頭に挿入
            if ans:
                temp = ans.pop()
                ans.insert(0, temp)
            # 先頭に挿入
            ans.insert(0, num)
        return ans
