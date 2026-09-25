# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getSum(head) -> int:
            if not head:
                return 0
            res = 0
            multiplier = 1
            cur = head
            while cur:
                res += cur.val * multiplier
                multiplier *= 10
                cur = cur.next
            return res
        
        list_sum = getSum(l1) + getSum(l2)
        head = ListNode(list_sum % 10)
        list_sum = list_sum // 10
        cur = head
        while list_sum > 0:
            new = ListNode(list_sum % 10)
            list_sum = list_sum // 10
            cur.next = new
            cur = cur.next
        return head

