class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num1 in nums1:
            exist_flag = False
            check_start_flag = False 
            for num2 in nums2:
                if num1 == num2:
                    check_start_flag = True
                if check_start_flag == True and num1  < num2:
                    result += [num2]
                    exist_flag =True
                    break
            if not exist_flag:
                result +=[-1]
        return result
