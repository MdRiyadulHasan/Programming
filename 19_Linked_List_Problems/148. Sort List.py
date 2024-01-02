# https://leetcode.com/problems/sort-list/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        list1 = self.sortList(head)
        list2 = self.sortList(mid)
        return self.merge(list1, list2)

    def merge(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next

# Example usage
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
solution = Solution()
sorted_list = solution.sortList(head)

print("Original Linked List:")
print_linked_list(head)

print("\nSorted Linked List:")
print_linked_list(sorted_list)

        