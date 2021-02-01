# -*- coding = utf-8 -*-
# @Time：2021-02-01 23:10
# @Author：来瓶安慕嘻
# @File：力扣33_旋转数组查找.py
# @开始美好的一天吧 @Q_Q@



def search(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]: # 若如目标值处于左边序列中
            r = mid - 1                   # 缩小范围，二分查找
        else:
            l = mid + 1
    return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums,target))