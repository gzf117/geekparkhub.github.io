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
# @Program : 异常处理和文件操作 | Exception Handling and File Operations
# @File : 12_exception_handling_and_file_operations.py
# @Description : Python 基础篇 - 异常处理和文件操作 | Python Basics-Exception Handling and File Operations

# 异常 | extremely
print('Extremely!')
try:
    # 捕获异常 | Catch exception
    print(10 / 0)
except:
    # 处理异常 | Handling exceptions
    print('Handling exceptions')
else:
    print('End')

print('Before the exception')
try:
    print(10 / 0)
# Exception是所有异常类的父类, 所以如果except后跟的是Exception则会捕获到所有的异常
except Exception as e:
    print('Exception Info', e)
finally:
    print('无论是否出现异常, 最终该语句都会执行')
print('After the exception')
