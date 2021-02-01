# -*- coding = utf-8 -*-
# @Time：2021-01-30 15:56
# @Author：来瓶安慕嘻
# @File：快速排序双指针法.py
# @开始美好的一天吧 @Q_Q@

def quick_sort(alist):
    return sort(alist,0,len(alist)-1)


def sort(alist,first,last):
    if first >= last:
        return alist
    left = first
    right = last
    mid = alist[first]
    while left < right:
        while left < right and alist[right] >= mid:
            right -= 1
        alist[left] = alist[right]

        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]

    alist[left] = mid

    sort(alist, first, left - 1)
    sort(alist, left + 1, last)


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist)
    print(alist)
