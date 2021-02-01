# -*- coding = utf-8 -*-
# @Time：2021-01-28 15:29
# @Author：来瓶安慕嘻
# @File：动态规划.py
# @开始美好的一天吧 @Q_Q@


# 动态规划法
def maxSubArray(nums):
    f = [0] * len(nums)
    if len(nums) == 1:
        return nums[0], f
    else:
        # 动态DP数组
        f[0] = nums[0]  # 边界条件
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1] + nums[i], nums[i])
            # 注意这里跟求数组中最大子数组(非连续)不同，非连续的话后面是f[i-1]，不是nums[i]
        return max(f), f


# 找到索引
def find_nums(nums, f):
    if len(nums) == 1:
        return 0
    else:
        nums_index = []
        maxf = max(f)
        ind = f.index(maxf)
        nums_index.append(ind)
        while f[ind] != nums[ind]:
            nums_index.append(ind - 1)
            ind -= 1
        nums_index.reverse()
        return nums_index


if __name__ == "__main__":
    nums =  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # print(sum(nums))
    # nums = [-1,3,-1]
    value, f = maxSubArray(nums)
    print(f)
    print(value)
    print(find_nums(nums, f))
