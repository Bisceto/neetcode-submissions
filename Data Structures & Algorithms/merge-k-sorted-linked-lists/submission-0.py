# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hm = defaultdict()
        min_heap = []
        dummy = ListNode(0)
        cur = dummy

        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap,(head.val, idx, head))
                if head.next:
                    hm[idx] = head.next
                else:
                    hm[idx] = None
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next
            if hm[idx] is not None:
                heapq.heappush(min_heap, (hm[idx].val, idx, hm[idx]))
                if hm[idx].next:
                    hm[idx] = hm[idx].next
                else:
                    hm[idx] = None
        return dummy.next
            