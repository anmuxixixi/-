# -*- coding = utf-8 -*-
# @Time：2021-01-25 18:45
# @Author：来瓶安慕嘻
# @File：字典的操作.py
# @开始美好的一天吧 @Q_Q@

# 创建新的字典
book_dict = {"price": 500, "bookName": "Python数据结构与算法", "weight": "250g"}
book_dict['page']="216页"

print(book_dict)

# 删除元素
# del book_dict['page']
# print(book_dict)

# print(book_dict.pop('bookName'))
# print(book_dict)

# book_dict.clear() # 清除字典中的所有元素

# 修改元素
# book_dict.update({'country':'中国'})
# book_dict.update({'page':'292页'})
#
# # 获取key的值
# print(book_dict['price'])

print(book_dict.get('page'))
#
# # 检查key是否存在
# print(book_dict.keys())
# print('price' in book_dict.keys())
# print('name' in book_dict)
#
# # 哈希表长度
# print(len(book_dict))

# # 遍历字典
# # 1.遍历键
# for key in book_dict:
#     print(key)
# print('=='*20)
#
# for key in book_dict.keys():
#     print(key)
# print('=='*20)
#
# # 2.遍历值
# for v in book_dict.values():
#     print(v)
# print('=='*20)
#
# # 3.遍历字典项
for kv in book_dict.items():
    print(kv)
print('=='*20)

# # 4.遍历键值对
# for k,v in book_dict.items():
#     print(k,v)
#
# print(book_dict.items())