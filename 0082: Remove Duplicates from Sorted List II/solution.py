# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        # 一つ目に0を挿入して、そこからwhile内を処理を行う
        before_node = ListNode(0)
        before_node.next = head
        node = before_node
        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                val = node.next.val
                while node.next and node.next.val == val:
                    node.next = node.next.next
            else:
                node = node.next
        return before_node.next
