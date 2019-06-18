# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2分木のランクを求める

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        rank = 0
        if root == None:
            return 0
        return max(self.maxDepth(root.left) + 1 , self.maxDepth(root.right) + 1)
