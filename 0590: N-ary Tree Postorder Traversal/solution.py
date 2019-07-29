"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.dfs(root)
        return self.ans
    
    def dfs(self, node):
        if not node:
            return
        
        for n in node.children:
            self.dfs(n)
        self.ans.append(node.val)
