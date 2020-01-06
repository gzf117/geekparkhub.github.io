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
