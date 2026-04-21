# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        #[2,4,6,8]
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #[2 -> 4] and [4 -> 8]
        second = slow.next #second = 6
        prev = slow.next = None # prev = 4 -> None

        while second: #[6 -> 8]
            temp = second.next # temp = 8
            second.next = prev # 6 -> None
            prev = second # 6 -> None
            second = temp # 8 -> None

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        
