class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_list = []
        even_list = []
        answer_list = []
        
        for number in A:
            if number % 2 == 0:
                odd_list += [number]
            else:
                even_list += [number]
        for number in range(len(A)):
            answer_list += [0]
        for i, number in enumerate(even_list):
            answer_list[2 * i + 1] = number
        for i, number in enumerate(odd_list):
            answer_list[2 * i] = number
        return answer_list
