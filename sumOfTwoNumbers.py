# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        temp = ListNode(0)
        temp = head
        carry_over = 0
        while(l1 or l2 or carry_over):
            temp_sum = 0
            x = (l1.val if l1 else 0)
            y = (l2.val if l2 else 0)
            carry_over, temp_sum = divmod(x + y + carry_over,10)
            temp.next = ListNode(temp_sum)
            temp = temp.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return head.next