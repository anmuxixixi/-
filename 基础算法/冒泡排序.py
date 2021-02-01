# -*- coding = utf-8 -*-
# @Time：2021-01-26 20:54
# @Author：来瓶安慕嘻
# @File：冒泡排序.py
# @开始美好的一天吧 @Q_Q@


def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        count = 0
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        if count == 0:
            break
    return alist


if __name__ == "__main__":
    print(bubble_sort([4, 1, 2, 7, 6, 0]))
    print(bubble_sort([0, 1, 2, 3]))
