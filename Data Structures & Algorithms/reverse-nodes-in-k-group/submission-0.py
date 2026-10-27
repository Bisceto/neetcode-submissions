# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        prevTail = sentinel
        cur = head
        while True:
            # current head of the reverse group
            curHead = cur
            # find the head of the next group
            nextHead = cur            
            for _ in range(k):
                if not nextHead:
                    return sentinel.next
                nextHead = nextHead.next
            
            # TODO: Reverse the reverse group until the node before nextHead
            prev = nextHead
            curNode = curHead
            while curNode != nextHead:
                nxt = curNode.next
                curNode.next = prev
                prev = curNode
                curNode = nxt
            newHead = prev
            newTail = curHead
            # Adjust the pointers: curHead (the new tail) is already pointing to next head
            # prevTail.next is now pointing to the new head
            # adjust cur to nextHead
            prevTail.next = newHead
            cur = nextHead
            prevTail = newTail
            
