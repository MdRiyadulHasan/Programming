from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# Example usage:
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
# Printing the original linked list
print("Original Linked List:")
print_linked_list(head)
solution = Solution()
new_head = solution.deleteDuplicates(head)
print("\nLinked List after Removing Duplicates:")
print_linked_list(new_head)
