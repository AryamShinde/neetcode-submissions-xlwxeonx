# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next # temp = None
            second.next = prev # 5 -> 4 -> None
            prev = second # prev = 5 -> 4 -> None
            second = temp # second = None

        first, second = head, prev #first = 1, 2, 3 and second = 5, 4

        while second:
            temp1, temp2 = first.next, second.next # temp1 = 3 and temp2 = None
            first.next = second # 2 -> 4
            second.next = temp1 # 4 -> 3
            first, second = temp1, temp2 # first = 1 -> 5 -> 2 -> 4 -> 3 and second = None 


