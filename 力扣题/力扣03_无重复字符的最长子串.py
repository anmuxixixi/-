# -*- coding = utf-8 -*-
# @Time：2021-02-01 12:56
# @Author：来瓶安慕嘻
# @File：力扣03_无重复字符的最长子串.py
# @开始美好的一天吧 @Q_Q@


def lengthOfLongestSubstring(s):
    res,left,right = 0,0,0
    for i,c in enumerate(s):
        if c not in s[left:right]:
            right += 1
        else:
            left += s[left:right].index(c) + 1  # 找到第一个重复值，并跳到下一个开始新的窗口
            right += 1
        res = max(res,right-left)
    return res


if __name__ == "__main__":
    s = "pwawkew"
    print(lengthOfLongestSubstring(s))