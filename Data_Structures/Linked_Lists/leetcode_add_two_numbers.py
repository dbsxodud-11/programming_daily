# LeetCode: Add Two Numbers
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next
    


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        orig_head = ListNode()
        head = orig_head

        add = 0
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            tail = ListNode()
            num = val1 + val2 + add
            if num >= 10:
                tail.val = num - 10 
                add = 1
            else:
                tail.val = num
                add = 0
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            head.next = tail
            head = tail

        if add == 1:
            head.next = ListNode(1)
        # print(orig_head.next.val)
        return orig_head.next
    

if __name__ == "__main__":
    test_cases = [[ListNode(2, next=ListNode(4, next=ListNode(3))), 
                   ListNode(5, next=ListNode(6, next=ListNode(4))), 
                   ListNode(7, next=ListNode(0, next=ListNode(8)))]]
    
    solution = Solution()
    
    fail = False
    for test_case in test_cases:
        if solution.addTwoNumbers(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break
    
    if not fail:
        print("SUCCESS")