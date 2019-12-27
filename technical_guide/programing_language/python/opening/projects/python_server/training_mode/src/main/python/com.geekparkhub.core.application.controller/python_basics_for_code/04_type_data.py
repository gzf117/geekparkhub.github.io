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
# @Program : 数据类型 | type of data
# @File : 04_type_data.py
# @Description : Python 基础篇 -  数据类型 | Python Fundamentals-Data Types

# 定义 整数 | Definition integer
object_widths = 18
# 如果数字的长度过大, 可以使用下划线作为分隔符 | If the number is too long, you can use an underscore as a separator
object_lengths = 18_15_16
print(object_widths * object_lengths)
print("------------------------------------------------------\n")

# 定义 浮点数 | Definition Floating point
assets = 5242414.455
incomes = 500.36
print(assets + incomes)
print("------------------------------------------------------\n")

# 定义 字符串 | Definition String
# 定义 (单引号)修饰字符串 | Define (single quote) decorated strings
saying = 'Le vent se lève, il faut tenter de vivre!\n'

# 定义 (双引号)修饰字符串 | Define (double quotes) decorated strings
quotes = "A man who is artistic for art often gets the most pleasure from the least important and mundane image!\n"

# 定义 (单引号嵌套双引号)修饰字符串 | Define (single-quoted nested double-quoted) decorated strings
talks = 'Arthur · Conan · Doyle: "Hard work creates talent!"\n'

# 定义 (三重引号)修饰长字符串 | Definition (triple quotes) to decorate long strings
fragment = '''We must go deep into life, 
Only then can you get novel effects and extraordinary cooperation, 
And this in itself is more irritating than any imagination!'''

print(saying, quotes, talks, fragment)
print("------------------------------------------------------\n")

# 定义 格式化 字符串 | Definition Format string
# 使用加号拼接字符串 | Use plus sign to concatenate strings
words = 'py' + 'thon'
nums = 666
print('words = ' + words)  # Output result: words = python
# 多个参数 | Multiple parameters
print('result = ', words, nums)  # Output result: result = 456
print("------------------------------------------------------\n")

# 在字符串中指定占位符 | Specifying placeholders in strings
word1 = 'odd_number= 135%s' % '7911'  # Output result: odd_number= 1357911
word2 = 'even_number= 24%s810%s' % ('6', '12')  # Output result: even_number= 24681012
word3 = 'assets= %.2f' % 555.456  # Output result: assets= 555.46
word4 = 'assets=  %d' % 555.95  # Output result: assets=  555

# 通过`f`来创建格式化字符串 | Create a formatted string with `f`
result = f'result= {word1} {word2}'  # Output result: result= odd_number= 1357911 even_number= 24681012
print(word1, word2, word3, word4, result)
print("------------------------------------------------------\n")

# 格式化 字符串综合练习 | Format string synthesis exercise
word = 'py' + 'thon'
print('人生苦短 ' + '快选 ' + word)
print('人生苦短', '快选', word)
print('人生苦短 快选 %s' % word)
print(f'人生苦短 快选 {word}')
print("------------------------------------------------------\n")

# 字符串 复制 (将字符串和数字相乘) | String copy (multiply strings and numbers)
info = 'Learning!\t'
info = info * 20
print(info)
print("------------------------------------------------------\n")

# 定义 转义字符 | Definition escape character
talk = 'Arthur · Conan · Doyle:\t "Hard work creates talent!\\"\n'
print(talk)
print("------------------------------------------------------\n")

# 定义 布尔值 | Definition Boolean value
print('True=', True)  # Output result: True
print('False=', False)  # Output result: False
print('3 > 2=', 3 > 2)  # Output result: True
print('3 < 2=', 3 < 2)  # Output result: False

print('True and True=', True and True)  # Output result: True
print('True and False=', True and False)  # Output result: False
print('3 < 2 and 3 < 2=', 3 < 2 and 3 < 2)  # Output result: False

print('True or True=', True or True)  # Output result: True
print('True or False=', True or False)  # Output result: True
print('3 < 2 or 3 < 2=', 3 < 2 or 3 < 2)  # Output result: False

print('not True=', not True)  # Output result: False
print('not False=', not False)  # Output result: True
print('not 3 > 2=', not 3 > 2)  # Output result: False

if 20 >= 18:
    print('大于等于')
else:
    print('小于等于')

print("------------------------------------------------------\n")

# 定义 空值 | Definition Null value
data = None
print(data)
print("------------------------------------------------------\n")

# 类型检查 | Type check
values1 = 123456  # Output result: <class 'int'>
values2 = '123456'  # Output result: <class 'str'>
values3 = None  # Output result: <class 'NoneType'>
values4 = True  # Output result: <class 'bool'>
values5 = 555.456  # Output result: <class 'float'>
print(type(values1), type(values2), type(values3), type(values4), type(values5))
