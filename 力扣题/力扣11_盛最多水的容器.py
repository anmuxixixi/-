# -*- coding = utf-8 -*-
# @Time：2021-01-31 21:26
# @Author：来瓶安慕嘻
# @File：力扣11_盛最多水的容器.py
# @开始美好的一天吧 @Q_Q@

"""

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，
垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

示例1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例2：
输入：height = [4,3,2,1,4]
输出：16

"""


# def maxArea(height):
#     i, j, res = 0, len(height) - 1, 0
#     while i < j:
#         if height[i] < height[j]:
#             res = max(res, height[i] * (j - i))
#             i += 1
#         else:
#             res = max(res, height[j] * (j - i))
#             j -= 1
#     return res


def maxArea(height):
    left,right = 0,len(height)-1
    res = 0
    while left<right:
        if height[left]<height[right]:
            res = max(res,height[left]*(right-left))
            left += 1
        else:
            res = max(res,height[right]*(right-left))
            right -= 1
    return res


if __name__ == "__main__":
    li = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # li = [4,3,2,1,4]
    print(maxArea(li))
