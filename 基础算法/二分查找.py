# -*- coding = utf-8 -*-
# @Time：2021-01-26 12:55
# @Author：来瓶安慕嘻
# @File：二分查找.py
# @开始美好的一天吧 @Q_Q@


def binary_search(alist, item):
    """递归二分查找"""
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)


def binary_search_two(alist,item):
    """双指针二分查找"""
    first = 0
    last = len(alist)-1
    while first < last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            last = mid
        else:
            first = mid+1
    return False  # 循环遍历完没有找到，返回False


if __name__ == "__main__":
    li = [1, 6, 10, 26, 45, 78, 99, 105,200]
    # print(binary_search(li, 1))
    # print(binary_search(li, 100))

    # print(binary_search_two(li,100))
    print(binary_search_two(li,26))
    print(binary_search_two(li,100))


