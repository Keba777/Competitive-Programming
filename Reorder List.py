# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        
