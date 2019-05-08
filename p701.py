# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current = root
        while current:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    return root
                current = current.left
            elif val > current.val:
                if not current.right:
                    current.right = TreeNode(val)
                    return root
                current = current.right
        return root
