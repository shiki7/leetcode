
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = []
        people.sort(key = lambda x: (-x[0], x[1]))
        for h, k in people:
            answer.insert(k, [h, k])
        return answer
