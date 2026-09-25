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
        #hm stores {Original Node, New Node}
        hm = defaultdict(Node)
        # Parse through the list once and add to hm
        cur = head
        while cur:
            copy = Node(cur.val)
            hm[cur] = copy
            cur = cur.next
        # Parse through the list again, set the randoms 
        cur = head
        while cur:
            if cur.next:
                hm[cur].next = hm[cur.next]
            if cur.random:
                hm[cur].random = hm[cur.random]
            cur = cur.next

        return hm[head]