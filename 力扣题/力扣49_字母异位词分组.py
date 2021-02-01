# -*- coding = utf-8 -*-
# @Time：2021-01-27 13:38
# @Author：来瓶安慕嘻
# @File：力扣49_字母异位词分组.py
# @开始美好的一天吧 @Q_Q@

"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。

"""


def groupAnagrams(strs):
    if len(strs)<2:
        return strs
    result = {}
    for s in strs:
        # sorted('ate') -> ['a','e','t'] 因此需要用join重新组合在一起
        tmp = ''.join(sorted(s))
        # 如果不存在排序后的key则返回[]，如果存在则拿到value值添加[s]
        result[tmp] = result.get(tmp,[])+[s]
        return list(result.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
