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
        node_pairs = {}

        def deepcopy(node):
            if not node:
                return None

            new_node = Node(node.val, deepcopy(node.next), None)
            if new_node:
                node_pairs[node] = new_node

            return new_node

        new_head = deepcopy(head)

        for node in node_pairs:
            if node.random:
                node_pairs[node].random = node_pairs[node.random]

        return new_head
