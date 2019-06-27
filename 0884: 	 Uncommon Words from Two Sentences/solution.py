class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        word_list = A.split(" ") + B.split(" ")
        dic = {}
        result = []
        for word in word_list:
            if word in dic.keys():
                dic[word] += 1
            else:
                dic[word] = 1
        for key, value in dic.items():
            if value == 1:
                result += [key]
        return result
