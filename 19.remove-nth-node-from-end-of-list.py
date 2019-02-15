#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (33.91%)
# Total Accepted:    347.4K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        nafter = dummy

        for i in range(n+1):
            nafter = nafter.next

        while(nafter):
            cur = cur.next
            nafter = nafter.next

        cur.next = cur.next.next 
        return dummy.next
