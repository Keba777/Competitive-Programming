# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(prev, cur):
            if not cur:
                return prev
            tail = rec(cur, cur.next)
            cur.next = prev

            return tail

        return rec(None, head)