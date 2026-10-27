# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Actually not needed, but the tracethrough is abit annoying
        if k == 1:
            return head
        sentinel = ListNode(0, head)
        prevTail = sentinel
        while True:
            # current head of the reverse group
            curHead = prevTail.next
            # find the head of the next group
            nextHead = curHead            
            for _ in range(k):
                if not nextHead:
                    return sentinel.next
                nextHead = nextHead.next
            
            # Reverse the reverse group
            prev = nextHead
            # Temporary cur to reverse the group
            cur = curHead
            while cur is not nextHead:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            # Adjust the pointers: curHead (the new tail) is already pointing to next head
            # prevTail.next is now pointing to the new  (which is prev)
            prevTail.next = prev
            prevTail = curHead
            
