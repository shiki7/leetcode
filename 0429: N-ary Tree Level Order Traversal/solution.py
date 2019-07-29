"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, node, level):
        if not node:
            return
        if len(self.ans)-1 < level:
            self.ans.append([])
        for n in node.children:
            self.dfs(n, level+1)
        self.ans[level].append(node.val)
