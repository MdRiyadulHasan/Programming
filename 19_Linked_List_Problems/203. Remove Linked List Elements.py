# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
solution = Solution()
print("Original Linked List:")
printLinkedList(head)
head = solution.removeElements(head, 6)
print("\nLinked List after removing nodes with value 6:")
printLinkedList(head)
