class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Check if there are at least k nodes remaining
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1

        # If there are fewer than k nodes, no need to reverse
        if count < k:
            return head

        # Reverse the group (basic way to reverse linked list)
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Recursively reverse the remaining groups
        print("Previous call", prev.val)
        head.next = self.reverseKGroup(curr, k)
        print(prev.val)
        return prev
        print(prev.val)

# Example usage:
def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
print("Original Linked List:")
printLinkedList(head)

# Reverse nodes in k-group (e.g., k=3)
sol = Solution()
new_head = sol.reverseKGroup(head, 3)

print("\nLinked List after reversing in k-group:")
printLinkedList(new_head)