# -*- coding = utf-8 -*-
# @Time：2021-01-30 13:49
# @Author：来瓶安慕嘻
# @File：希尔排序.py
# @开始美好的一天吧 @Q_Q@

def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            for j in range(i,0,-gap):
                if alist[j]<alist[j-gap]:
                    alist[j-gap], alist[j] = alist[j], alist[j-gap]
                else:
                    break
        gap = gap // 2  # 更新步长


if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    shell_sort(alist)
    print(alist)