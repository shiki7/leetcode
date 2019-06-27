# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tempNode = curNode = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curNode.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                curNode.next = ListNode(l2.val)
                l2 = l2.next
            curNode = curNode.next
        while l1:
            curNode.next = ListNode(l1.val)
            l1 = l1.next
            curNode = curNode.next
        while l2:
            curNode.next = ListNode(l2.val)
            l2 = l2.next
            curNode = curNode.next
        return tempNode.next
