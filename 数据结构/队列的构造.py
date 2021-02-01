# -*- coding = utf-8 -*-
# @Time：2021-01-18 23:07
# @Author：来瓶安慕嘻
# @File：队列的构造.py
# @开始美好的一天吧 @Q_Q@

class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
