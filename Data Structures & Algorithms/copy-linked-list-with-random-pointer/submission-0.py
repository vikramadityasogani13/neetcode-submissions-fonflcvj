"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new = {}
        curr = head
        while curr:
            new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = new[curr]
            copy.next = new.get(curr.next)
            copy.random = new.get(curr.random)
            curr = curr.next
        return new[head]