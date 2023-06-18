#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()  # Dummy node to simplify the code
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        sum_val = carry

        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next

        carry = sum_val // 10
        digit = sum_val % 10

        current.next = ListNode(digit)
        current = current.next

    return dummy.next

