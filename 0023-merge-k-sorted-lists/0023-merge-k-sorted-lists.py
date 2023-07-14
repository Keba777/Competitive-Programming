# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Push the first node from each list into the min heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        # Create a dummy node to build the merged list
        dummy = ListNode(0)
        curr = dummy
        
        # Pop the smallest node from the min heap and add it to the merged list
        while min_heap:
            val, i = heapq.heappop(min_heap)
            curr.next = ListNode(val)
            curr = curr.next
            
            # Push the next node from the list into the min heap
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return dummy.next
