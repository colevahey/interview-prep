# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None

        node = head
        previous = None

        while node != None:
            next_node = node.next
            node.next = previous
            previous = node
            node = next_node

        return previous
