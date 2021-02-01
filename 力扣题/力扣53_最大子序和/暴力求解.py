# -*- coding = utf-8 -*-
# @Time：2021-01-28 14:36
# @Author：来瓶安慕嘻
# @File：暴力求解.py
# @开始美好的一天吧 @Q_Q@


""""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""
from math import inf


def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    result = - inf
    for i in range(len(nums)):
        sums = 0
        for j in range(i, len(nums)):
            sums = sums + nums[j]
            result = max(result, sums)
    return result


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
