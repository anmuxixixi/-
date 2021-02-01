# -*- coding = utf-8 -*-
# @Time：2021-01-28 20:45
# @Author：来瓶安慕嘻
# @File：分治法.py
# @开始美好的一天吧 @Q_Q@


def maxSubArray(nums):
    n = len(nums)
    # 递归终止条件
    if n == 1:
        return nums[0]

    mid = n//2
    max_left = maxSubArray(nums[:mid])
    max_right = maxSubArray(nums[mid:])

    # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
    max_l = nums[mid-1]
    tmp = 0
    for i in range(mid-1,-1,-1):
        tmp += nums[i]
        max_l = max(tmp,max_l)

    max_r = nums[mid]
    tmp = 0
    for i in range(mid, n):
        tmp += nums[i]
        max_r = max(tmp, max_r)
    # 返回三个中的最大值
    return max(max_right, max_left, max_l + max_r)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-2,1,-3,4]
    print(maxSubArray(nums))