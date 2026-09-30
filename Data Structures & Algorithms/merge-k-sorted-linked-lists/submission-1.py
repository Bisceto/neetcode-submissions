# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        dummy = ListNode(0)
        cur = dummy

        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap,(head.val, idx, head))
       
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        return dummy.next
            