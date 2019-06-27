# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_check = (not root.left or root.val == root.left.val and self.isUnivalTree(root.left))
        right_check = (not root.right or root.val == root.right.val and self.isUnivalTree(root.right))
        return left_check and right_check
