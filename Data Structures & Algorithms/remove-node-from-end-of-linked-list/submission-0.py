# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        prev_l = None
        l = head
        r = head
        for i in range(n - 1):
            r = r.next
        print(l.val, r.val)
        while r.next:
            prev_l = l
            l = l.next
            r = r.next
        if prev_l:
            prev_l.next = l.next
            return head
        else:
            return l.next

        
        

