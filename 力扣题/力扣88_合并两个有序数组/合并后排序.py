# -*- coding = utf-8 -*-
# @Time：2021-01-31 14:20
# @Author：来瓶安慕嘻
# @File：合并后排序.py
# @开始美好的一天吧 @Q_Q@

def merge(nums1, m, nums2, n):
    """
        Do not return anything, modify nums1 in-place instead.
    """
    nums1 = sorted(nums1[:m] + nums2)
    return nums1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    # merge(nums1, m, nums2, n)
    # print(nums1)
    print(merge(nums1, m, nums2, n))
