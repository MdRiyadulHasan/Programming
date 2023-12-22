# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/

from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reversedList(node):
            prev = None 
            while node:
                nextNode = node.next 
                node.next = prev 
                prev = node 
                node = nextNode
            return prev
        def doubleList(node):
            carry = 0
            while node:
                total = (node.val)*2+carry
                rem = total%10
                carry = total//10
                node.val=rem
                pre = node
                node = node.next
            if carry:
                pre.next= ListNode(carry)
        reversedHead = reversedList(head)
        doubleList(reversedHead)
        result = reversedList(reversedHead)
        return result
linked_list = ListNode(9, ListNode(7, ListNode(9)))


solution = Solution()

# Print the original linked list
print("Original Linked List:")
current = linked_list
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# Call the plusOne function
result = solution.doubleIt(linked_list)

# Print the result
print("\nResult Linked List:")
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")



