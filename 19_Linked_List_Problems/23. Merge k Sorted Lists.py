# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if lists else None

    def mergeTwoLists(self, list1, list2):
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
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next

# Example usage
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create example linked lists: 1 -> 4 -> 5, 1 -> 3 -> 4, 2 -> 6
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6)),
]

solution = Solution()

# Merge the linked lists
merged_list = solution.mergeKLists(lists)

# Print the original and merged linked lists
print("Original Linked Lists:")
for lst in lists:
    print_linked_list(lst)

print("\nMerged Linked List:")
print_linked_list(merged_list)
