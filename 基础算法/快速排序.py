# -*- coding = utf-8 -*-
# @Time：2021-01-30 15:23
# @Author：来瓶安慕嘻
# @File：快速排序.py
# @开始美好的一天吧 @Q_Q@

def quick_sort(alist):
    if len(alist) < 2:
        return alist
    else:
        mid = alist[0]
        low = [x for x in alist[1:] if x <= mid]
        high = [x for x in alist[1:] if x > mid]
        return quick_sort(low) + [mid] + quick_sort(high)


if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    print(quick_sort(alist))