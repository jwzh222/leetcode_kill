#!/usr/bin/env python
# encoding: utf-8


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
    def ListToNum(self, l):
        p = ListNode(None)
        p = l
        result = 0
        while(p.next!=None):
            result = result*10 + p.value
        return result

    def NumToLink(self, num):
        parseList = parseNum(num)
        link = listToLink(parseList)
        return link.next

    def listToLink(self, parseL):
        head = ListNode(None)
        tail = head
        for x in parseL:
            node = ListNode(x)
            tail.next = node
            tail = node
        return head


    def parseNum(self, num):
        l = []
        while(num):
            l.append(num % 10)
            num = num / 10
        return l[::-1]


