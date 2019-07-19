# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.list = []
        
        def search(root):
            if root.left:
                search(root.left)
            self.list.append(root.val)
            if root.right:
                search(root.right)
        search(root)
        return self.list
