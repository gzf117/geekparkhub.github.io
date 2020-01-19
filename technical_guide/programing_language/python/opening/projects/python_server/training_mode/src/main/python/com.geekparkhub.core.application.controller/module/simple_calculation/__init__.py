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
# @Program : 包 | Package
# @File : __init__.py.py
# @Description : Python 基础篇 - 包 | Python Basics-Packages

# 导入子模块 | Import submodule
from module.simple_calculation.addition_calculation import addition_calculation_function as acf
from module.simple_calculation.subtraction_calculation import subtraction_calculation_function as scf
from module.simple_calculation.multiplication import multiplication_function as mf
from module.simple_calculation.division_calculation import division_calculation_function as dcf

# 调用 简易加法函数 | Call simple addition function
acf(10, 20)

# 调用 简易减法函数 | Call simple subtraction function
scf(60, 10)

# 调用 简易乘法函数 | Call simple multiplication function
mf(10, 10)

# 调用 简易除法函数 | Call simple division function
dcf(81, 9)
