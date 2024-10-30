# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode()  # Placeholder node to start the result list
        current = dummy_head
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = carry + x + y
            carry = total // 10

            # Add the current digit to the new linked list
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes in l1 and l2 if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # If there's a carry left after the loop, add it as a new node
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next  # Return the head of the resulting list
