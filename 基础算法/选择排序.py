# -*- coding = utf-8 -*-
# @Time：2021-01-30 11:19
# @Author：来瓶安慕嘻
# @File：选择排序.py
# @开始美好的一天吧 @Q_Q@


def select_sort(alist):
    for i in range(len(alist) - 1):
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


if __name__ == "__main__":
    print(select_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
