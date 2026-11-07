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
        if head == None:
            return None
        map_to_old = {}
        current = head
        while current:
            map_to_old[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            current_node = map_to_old.get(current)
            if current.next:
                current_node.next = map_to_old.get(current.next)
            if current.random:
                current_node.random = map_to_old.get(current.random)
            current = current.next
        return map_to_old.get(head)