# -*- coding:utf-8 -*-
# 
# Geek International Park | 极客国际公园
# GeekParkHub | 极客实验室
# Website | https://www.geekparkhub.com
# Description | Open · Creation | 
# Open Source Open Achievement Dream, GeekParkHub Co-construction has never been seen before.
# HackerParkHub | 黑客公园
# Website | https://www.hackerparkhub.org
# Description | In the spirit of fearless exploration, create unknown technology and worship of technology.
# GeekDeveloper : JEEP-711
# 
# @Author : system
# @Version : 0.2.5
# @Program : 数据结构集合 | Data structure collection
# @File : 09_data_structure_collection.py
# @Description : Python 基础篇 - 流程控制 | 数据结构集合 | Python Basics-Flow Control | Data Structure Collection

# 定义 列表 | Definition list
list1 = [1, 2, 3, 4, 5]

# 获取列表元素长度 | Get list element length
print('lens=', len(list1))

# 访问列表中的值 | Access value in list
print(list1[1])

# 更新列表 | update list
list1.append(6)

# 删除列表元素 | Remove list element
del list1[2]
print(list1)

# 定义 列表切片 | Definition list slice
# 如果省略结束位置则会一直截取到最后 | If the end position is omitted, it will be intercepted to the end.
print('list1[1:]: ', list1[1:])
# 如果省略起始位置则会从第一个元素开始截取 | If the starting position is omitted, it will be truncated from the first element
print('list1[:3]: ', list1[:3])
# 如果起始位置和结束位置全部省略则相当于创建一个列表的副本
print('list1[:]: ', list1[:])
# 通过切片获取元素时会包括起始位置的元素,不会包括结束位置的元素
print('list1[1:5]: ', list1[1:5])
# 定义 步长 | Definition Stride
print('list1[1:4:1]: ', list1[1:4:1])
print('list1[::1]: ', list1[::-1])

# 定义 列表 | Definition list
list2 = [1, 2, 3, 4, 5, 6]
list3 = ['C', 'C++', 'C#', 'Html', 'Java', 'PHP', 'Python', 'Scala', 'GoLang', 'R', 'Ruby', 'SQL']

# 定义 元素是否存在于列表中 | Defines whether the element exists in the list
print('Python' in list3)
print('Python' not in list3)

# 定义 迭代 | Definition iteration
for data in list3:
    print('data=', data)

# 定义 组合列表 | Definition Combination list
list2 = [1, 2, 3, 4, 5, 6] + [7, 8, 9, 10, 11]

# 定义 重复列表 | Definition repeat list
list3 = list3 * 4

# 获取列表长度 | Get list length
print('list2 length=', len(list2))
print('list3 length=', len(list3))
