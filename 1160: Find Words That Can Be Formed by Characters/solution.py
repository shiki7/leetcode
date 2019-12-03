class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sorted_chars = sorted(chars)
        ans = 0
        for word in words:
            sorted_word = sorted(word)
            cur = 0
            
            count = 0
            for alpha in sorted_word:
                flag = False
                for i in range(cur, len(sorted_chars)):
                    if sorted_chars[i] == alpha:
                        flag = True
                        count += 1
                        cur = i+1
                        break
                if not flag:
                    break
            if count == len(word):
                ans += len(word)
        return ans
