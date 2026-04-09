"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}

        def dfs(i):
            if i in oldToNew :
                return oldToNew[i]

            copy = Node(i.val)
            oldToNew[i] = copy

            for neighbor in i.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        return dfs(node)
        
