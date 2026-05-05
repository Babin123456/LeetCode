class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: find length
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        # Step 2: make cycle
        tail.next = head
        
        # Step 3: find new tail
        k = k % n
        steps = n - k - 1
        
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next
        
        # Step 4: break cycle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head