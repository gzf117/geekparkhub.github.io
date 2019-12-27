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
# @Program : 标识符 & 命名规范 | Identifiers & naming conventions
# @File : 03_Identifier_naming_convention.py
# @Description : Python 基础篇 - 标识符 & 命名规范 | Python Basics-Identifiers & Naming Conventions

# 定义 标识符 | Definition identifier

# 定义变量 | Defining variables
person_name = 'Jerry'
person_sex = 'man'
person_age = 20


# 定义函数 | Defining functions
def persons_info(name, sex, age):
    print("PersonName: " + name, ", PersonSex: " + sex, ", PersonAge:", age)
    return


# 调用函数 | call function
persons_info(person_name, person_sex, person_age)


# 定义 命名规范 | Definition Naming Convention
# 定义 下划线命名法 | Defining Underscore nomenclature
def addition_calculation(num1, num2):
    print("Result =", num1 + num2)
    return


# 调用函数 | call function
addition_calculation(100, 100)


# 定义 帕斯卡命名法 | Definition Pascal nomenclature
def MultiplicationCalculation(num1, num2):
    print("Result =", num1 * num2)
    return


# 调用函数 | call function
MultiplicationCalculation(100, 100)
