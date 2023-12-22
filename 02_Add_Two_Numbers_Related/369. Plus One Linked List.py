# https://leetcode.com/problems/plus-one-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # Reverse the linked list
        def reversedList(node):
            prev = None
            while node:
                nextNode = node.next
                node.next = prev 
                prev = node 
                node = nextNode
            return prev

       
        # Add one to the reversed linked list
        def addOne(node):
            carry = 1 
            while carry and node:
                total = node.val + carry 
                rem = total%10 
                carry = total//10
                node.val = rem 
                pre = node
                node = node.next
            if carry:
                pre.next = ListNode(carry)

        # Reverse the linked list back
        reversedHead = reversedList(head)
        addOne(reversedHead)
        result = reversedList(reversedHead)
        return result


linked_list = ListNode(9, ListNode(9, ListNode(9)))


solution = Solution()

# Print the original linked list
print("Original Linked List:")
current = linked_list
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# Call the plusOne function
result = solution.plusOne(linked_list)

# Print the result
print("\nResult Linked List:")
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
