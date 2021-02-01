# -*- coding = utf-8 -*-
# @Time：2021-01-31 13:02
# @Author：来瓶安慕嘻
# @File：验证Python.py
# @开始美好的一天吧 @Q_Q@


a = [1,2,4]
print(id(a))  # 1470960525832



a = []
print(id(a)) # 2774197297736
print(a)
a.append(1)
print(id(a)) # 2774197297736

a[:] = []
print(id(a))  # 1470960525832