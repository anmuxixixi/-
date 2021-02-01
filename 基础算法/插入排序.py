# -*- coding = utf-8 -*-
# @Time：2021-01-30 12:14
# @Author：来瓶安慕嘻
# @File：插入排序.py
# @开始美好的一天吧 @Q_Q@


def insert_sort(alist):
    for i in range(1,len(alist)):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j-1],alist[j]=alist[j],alist[j-1]
            else:
                break
    return alist


if __name__ == "__main__":
    print(insert_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
