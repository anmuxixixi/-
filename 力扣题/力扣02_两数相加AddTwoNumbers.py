# -*- coding = utf-8 -*-
# @Time：2021-01-15 15:16
# @Author：来瓶安慕嘻
# @File：力扣02_两数相加AddTwoNumbers.py
# @开始美好的一天吧 @Q_Q@

"""

给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。

示例1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例2：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

"""
from Cython.Compiler.ExprNodes import ListNode

#
# def addTwoNumbers(l1,l2):
#     res = ListNode()
#     cur = res
#     digit = 0


a = [1,2,3,2,4]
a.insert(2,5)
# a.remove(2)
print(a)
index = a.index(2)
print(index)