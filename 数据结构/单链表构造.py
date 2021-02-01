# -*- coding = utf-8 -*-
# @Time：2021-01-16 9:44
# @Author：来瓶安慕嘻
# @File：单链表构造.py
# @开始美好的一天吧 @Q_Q@

class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单向链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None  # 只需判断头节点是否为空即可

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem,end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素"""
        if pos <= 0:  # 如果输入的是小于等于零的数，则相当于头插
            self.add(item)
        elif pos > self.length(): # 如果输入的位置大于当前链表的长度，则相当于尾插
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                pre = pre.next
                count += 1
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        # 要把cur理解成一个游标 游标有两个属性,一个是elem,一个是next
        while cur is not None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 如果是头节点
                if pre is None:
                    self.__head = cur.next
                # 如果不是头节点
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self,item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    # node = Node(2)
    ll = SingleLinkList()
    # ll.append(10)
    # ll.append(12)
    # ll.travel()
    print(ll.length())