# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        cur = head
        nxt = head.next
        while nxt:
            cur.next = prev
            prev = cur
            temp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = temp
        return cur
