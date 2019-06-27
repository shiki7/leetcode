# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digit = 0
        sum = 0
        up = 0
        while l1 or l2 or up != 0:
            add_val = 0
            if l1 and l2 :
                add_val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2 == 0:
                add_val = l1.val
                l1 = l1.next
            elif not l1 and l2:
                add_val = l2.val
                l2 = l2.next
            add_val += up
            value = add_val % 10  
            up = int(add_val / 10)
            sum += 10**digit * value
            digit += 1
        str_sum = str(sum)[::-1]
        list = []
        for s in str_sum:
            list.append(int(s))
        return list
