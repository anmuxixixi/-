# -*- coding = utf-8 -*-
# @Time：2021-01-17 23:01
# @Author：来瓶安慕嘻
# @File：栈的构造.py
# @开始美好的一天吧 @Q_Q@

class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加新的元素item到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素的个数"""
        return len(self.__list)

    def travel(self):
        """遍历栈的元素"""
        while self.__list:
            print(self.pop(),end=" ")
        print("")


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.travel()
