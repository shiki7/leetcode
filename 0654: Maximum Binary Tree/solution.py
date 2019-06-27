# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
        
        max_num = max(nums)
        max_index = nums.index(max_num)
        node = TreeNode(max_num)
        if (len(nums[:max_index])):
            node.left = self.constructMaximumBinaryTree(nums[:max_index])
        if (len(nums[max_index+1:])):
            node.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return node
