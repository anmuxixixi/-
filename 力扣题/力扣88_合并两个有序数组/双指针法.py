# -*- coding = utf-8 -*-
# @Time：2021-01-31 13:29
# @Author：来瓶安慕嘻
# @File：双指针法.py
# @开始美好的一天吧 @Q_Q@

# 个人推荐双指针写法，更加通俗易懂
def merge(nums1, m, nums2, n):
    nums1_copy = nums1[:m]
    nums1 = []

    p1, p2 = 0, 0
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1
    nums1 += nums1_copy[p1:]
    nums1 += nums2[p2:]
    print(nums1)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
