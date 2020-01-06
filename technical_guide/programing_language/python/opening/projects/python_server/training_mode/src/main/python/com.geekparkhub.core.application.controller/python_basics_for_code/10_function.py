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
# @Program : 函数 | function
# @File : 10_function.py
# @Description : Python 基础篇 - 函数 | Python Basics-Functions


# 定义函数 | Defining functions
def functions():
    print('\nI am a function !\n')


# 调用函数 | call function
functions()


# 定义函数 | Defining functions
def functions1(num1, num2, num3=30):
    print('res=', num1 * num2 * num3)


# 调用函数 | call function
functions1(10, 20)


# 定义函数 | Defining functions
def functions2(num):
    # 在函数中对形参进行重新赋值, 不会影响其他的变量
    # a = 20
    # num是一个列表尝试修改列表中的元素
    # 如果形参执行的是一个对象，可以通过形参去修改对象时, 会影响到所有指向该对象的变量
    num[0] = 30
    print('num =', num, id(num))


values = 10
values = [1, 2, 3]

# 调用函数 | call function
functions2(values)
functions2(values.copy())
functions2(values[:])


# 定义函数 | Defining functions
# `*num1` 将接受所为位置参数并且会将实参统一保存元祖中
def functions3(*nums1):
    print('nums1=', nums1, 'type=', type(nums1))


# 调用函数 | call function
functions3()
functions3(1, 3, 5, 7, 9)


# 定义函数 | Defining functions
def functions4(*nums):
    res = 0  # 定义初始化变量, 保存结果集
    for data in nums:
        res += data
    print('res=', res)


# 调用函数 | call function
functions4(6)
functions4(6, 6)
functions4(6, 6, 6)
functions4(6, 6, 6, 6)
functions4(6, 6, 6, 6, 6)


# 定义函数 | Defining functions
# `**` 形参可以接收其他关键字参数, 它将这些参数保存在字典中
# 字典中keys就是参数的名字, 字典中values就是参数的值
def functions5(**nums):
    print('**nums=', nums, 'type=', type(nums))


# 调用函数 | call function
functions5()


# 定义函数 | Defining functions
def functions6(nums1, nums2, nums3):
    print('sum=', nums1 + nums2 + nums3)


# 定义 元祖 | Definition Tuple
tuples = (10, 10, 10)
# 调用函数 | call function
# 传递参数时,可以在序列类型参数前添加`*`星号,这样称之为参数解包,会自动将序列中的元素依次作为参数传递
functions6(*tuples)


# 定义函数 | Defining functions
def functions7(nums1, nums2, nums3):
    print('nums1=', nums1, 'nums2=', nums2, 'nums3=', nums3)


# 定义字典 | Definition Dictionary
dictionary = {'nums1': '1', 'nums2': '2', 'nums3': '3'}
# 调用函数 | call function
# 通过`**`对字典进行解包操作
functions7(**dictionary)
