# -*- coding = utf-8 -*-
# @Time：2021-01-30 23:06
# @Author：来瓶安慕嘻
# @File：从后向前的双指针.py
# @开始美好的一天吧 @Q_Q@


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    p1 = m - 1
    p2 = n - 1

    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    # nums1[:p2 + 1] = nums2[:p2 + 1]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
