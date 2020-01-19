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
# @Program : 模块 | Module
# @File : core_module.py
# @Description : Python 基础篇 - 模块 | Python Basics-Modules

# 创建模块 | Create module

# 定义变量 | Defining variables
nums1 = 100
nums2 = 200
_nums3 = 300


# 定义 函数 | Definition function
def core_module_function():
    print('core_module_function!')


# 定义 类 | Definition class
class CoreModule:
    # 定义 初始化方法 | Definition initialization method
    def __init__(self, info):
        self._info = info

    # 定义 getter&setter方法 | Define getter & setter method
    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info


'''
检查当前模块是否为主模块, 为主模块时才需执行
'''
if __name__ == '__main__':
    core_module_function()
    c = CoreModule('CoreModule')
    print('c.info=', c.info)
