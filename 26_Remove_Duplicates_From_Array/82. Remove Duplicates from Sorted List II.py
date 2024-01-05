# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                current = current.next
                prev.next = current
            else:
                current = current.next
                prev = prev.next

        return dummy.next

# Example usage:
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creating a sorted linked list with duplicates
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

# Printing the original linked list
print("Original Linked List:")
print_linked_list(head)

# Applying the deleteDuplicates method
solution = Solution()
new_head = solution.deleteDuplicates(head)

# Printing the linked list after removing duplicates
print("\nLinked List after Removing Duplicates:")
print_linked_list(new_head)
