# -*- coding = utf-8 -*-
# @Time：2021-01-19 10:43
# @Author：来瓶安慕嘻
# @File：力扣21_合并两个有序链表.py
# @开始美好的一天吧 @Q_Q@
from Cython.Compiler.ExprNodes import ListNode


def mergeTwoList(l1,l2):
    res = ListNode(0)
    cur = res
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return res.next

l1 = ListNode(1)
l2 = ListNode(4)
print(mergeTwoList(l1,l2))