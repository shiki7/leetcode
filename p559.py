"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        current_max_depth = 0
        if root is None:
            return 0
        for child in root.children:
            current_max_depth = max(self.maxDepth(child), current_max_depth)
        return current_max_depth + 1
