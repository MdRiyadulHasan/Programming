class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def sortList(self, head):
    if not head or not head.next:
        return head 
    slow = head 
    first = head.next 
    while first and first.next:
        slow = slow.next 
        first = first.next.next 
    mid = slow.next 
    slow.next = None 
    
    left = self.sortList(head)
    right = self.sortList(mid)
    return self.merge(left,right)

def merge(self, l1, l2):
    dummy = ListNode(0)
    current = dummy 
    while l1 and l2:
        if l1.val<=l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next