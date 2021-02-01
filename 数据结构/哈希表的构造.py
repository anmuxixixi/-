# -*- coding = utf-8 -*-
# @Time：2021-01-24 21:28
# @Author：来瓶安慕嘻
# @File：哈希表的构造.py
# @开始美好的一天吧 @Q_Q@

class LinkList(object):
    class Node:
        """创建节点类"""

        def __init__(self, item):
            self.item = item
            self.next = None

    class LinkListIterator:
        """创建链表迭代器"""

        def __init__(self, node):
            self.node = node

        def __next__(self):
            """
            next和iter组成了class中的一个迭代器，使用私有属性后会自动进行迭代
            """
            # 当链表中存在元素就会不断就行迭代
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    # def __init__(self, iterable=None):
    #     self.head = None
    #     self.tail = None
    #     if iterable:
    #         self.extend(iterable)

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s  # 指针偏移

    # def extend(self, iterable):
    #     for obj in iterable:
    #         self.append(obj)

    def find(self, obj):
        cur = self.head
        while cur is not None:
            if cur.item == obj:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, obj):
        if self.find(obj):
            """删除节点"""
            cur = self.head
            pre = None
            while cur is not None:
                if cur.item == obj:
                    # 先判断此节点是否是头节点
                    # 如果是头节点
                    if pre is None:
                        self.head = cur.next
                    # 如果不是头节点
                    else:
                        pre.next = cur.next
                    break
                else:
                    pre = cur
                    cur = cur.next

        else:
            print(obj, '不存在！')

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "[" + "→".join(map(str, self)) + ']'


class HashTable(object):
    """创建哈希表"""

    def __init__(self, size=100):
        self.size = size
        self.hashlist = [LinkList() for i in range(self.size)]

    def hash(self, k):
        # 求k的hash函数值
        return k % self.size

    def insert(self, k):
        # 在第i个位置的链表后尾插k
        i = self.hash(k)
        if self.find(k):
            print(str(k) + ' 已存在')
        else:
            self.hashlist[i].append(k)

    def find(self, k):
        # 查看元素是否已经存在于内存空间中
        i = self.hash(k)
        return self.hashlist[i].find(k)

    def delete(self,k):
        i = self.hash(k)
        return self.hashlist[i].remove(k)


if __name__ == "__main__":
    ht = HashTable()
    ht.insert(0)
    ht.insert(1)
    ht.insert(2)
    ht.insert(100)
    ht.insert(200)
    ht.insert(500)
    print(ht.hashlist[0])
    print(ht.find(100))
    ht.delete(5)
    print(ht.hashlist[0])

