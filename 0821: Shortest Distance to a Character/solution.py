class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        result = []
        for index, char in enumerate(S):
            # 該当文字のとき0
            if char == C:
                result += [0]
                continue
            # インデックスから左、右をそれぞれチェックして最短の距離を求める
            distance_left = 0
            distance_right = 0
            flag_left = False
            flag_right = False
            # left_check
            if index >= 1:
                for left_index in range(index, -1 , -1):
                    if S[left_index] == C:
                        flag_left = True
                        break
                    distance_left += 1
            # right_check
            if index < len(S) - 1:
                for right_index in range(index, len(S) ):
                    if S[right_index] == C:
                        flag_right = True
                        break
                    distance_right += 1
                        
            if index == 0 or flag_left == False:
                result += [distance_right]
            elif index >= len(S) - 1 or flag_right == False:
                result += [distance_left]
            else:
                result += [min(distance_left, distance_right)]
        return result
