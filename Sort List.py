# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = tail = ListNode(None)
        while left and right:
            if left.val < right.val:
                tail.next, tail, left = left, left, left.next
            else:
                tail.next, tail, right = right, right, right.next
        tail.next = left or right
        return dummy.next
