"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Rnutime Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node_pairs = {}

        curr = head
        while curr:
            node_pairs[curr] = Node(curr.val)
            curr = curr.next

        for node in node_pairs:
            if node.next:
                node_pairs[node].next = node_pairs[node.next]
            if node.random:
                node_pairs[node].random = node_pairs[node.random]

        return node_pairs[head]
