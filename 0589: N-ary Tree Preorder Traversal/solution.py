"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ans = []
        
        def dfs(node: 'Node'):
            if node:
                self.ans += [node.val]
                for child in node.children:
                    dfs(child)
        dfs(root)
        return self.ans
