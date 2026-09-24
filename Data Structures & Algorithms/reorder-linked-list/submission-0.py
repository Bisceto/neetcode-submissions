# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle node
        if not head:
            return None
        slow = head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle node now. end of the first half
        second_head = slow.next
        slow.next = None
        
        # Step 2: Reverse the second half
        prev = None
        cur = second_head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        #prev should be the end of the 
        
        # Step 3: Weave head and the reversed second half
        dummy = head
        while dummy and prev:
            temp = dummy.next
            dummy.next = prev
            dummy = dummy.next
            prev = prev.next
            dummy.next = temp
            dummy = dummy.next