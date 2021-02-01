# -*- coding = utf-8 -*-
# @Time：2021-02-01 17:16
# @Author：来瓶安慕嘻
# @File：力扣56_合并区间.py
# @开始美好的一天吧 @Q_Q@


"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

"""


def merge(intervals):
    result = []
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    for interval in intervals:
        if len(result)==0 or interval[0]>result[-1][1]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1],interval[1])
    return result


if __name__ == "__main__":
    intervals = [[2, 6], [8, 10],[1, 3], [15, 18]]
    print(merge(intervals))
    li = [[1,4],[2,3]]
    print(merge(li))