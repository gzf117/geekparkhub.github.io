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
# @Program : 运算符 | Operator
# @File : 07_operator.py
# @Description : Python 基础篇 - 运算符 | Python Fundamentals-Operators

# 运算符 | Operator

# 算术运算符 | Arithmetic operator
# (`+` 加法运算符) | (`-` 减法运算符) | (`*` 乘法运算符) | (`**` 幂运算) | (`/` 除法运算符) | (`//` 整除运算符) | (`%` 取余运算符)
nums = ((12 + 12 - 10) * 12) // 2
print('result=', nums)

# 赋值运算符 | Assignment operator
# (`=` 将等号右侧值赋给等号左侧变量) | (`+=` 等价于 `x = x + 1`) | (`-=` 等价于 `x = x - 1`) | (`*=` 等价于 `x = x * 1`)
# (`**=` 等价于 `x = x ** 1`) | (`/=` 等价于 `x = x / 1`) | (`//=` 等价于 `x = x // 1`) | (`%=` 等价于 `x = x % 1`)
nums1 = 1
nums1 += 100
nums1 -= 1
nums1 *= 1
nums1 **= 2
nums1 /= 10
nums1 //= 16
nums1 %= 12
print('result=', nums1)

# 关系运算符 | Relational operator
# (`>` 大于运算符) | (`>=` 大于等于运算符) | (`<` 小于运算符) | (`<=` 小于运算符)
# (`==` 等于运算符) | (`!=` 不等于运算符) | (`is` 比较两个对象是否是同一对象) | (`is not` 比较两个对象是否不是同一对象)
nums2 = 10 > 20
nums2 = 10 >= 20
nums2 = 10 < 20
nums2 = 10 <= 20
nums2 = '10' == '20'
nums2 = '10' != '20'
print('result=', nums2)

# 逻辑运算符 | Logical Operators
# (`not` 逻辑非) | (`and` 逻辑与) | (`or` 逻辑或) |
nums3 = True
# not可以对符号右侧的值进行非运算, 对于布尔值非运算会对其进行取反操作, True变False, False变True, 对于非布尔值非运算会先将其转换为布尔值然后再取反
nums3 = not nums3
# and可以对符号两侧的值进行与运算, 只有在符号两侧的值都为True时才会返回True, 只要有一个False就返回False
nums3 = True and True
nums3 = True and False
# or可以对符号两侧的值进行或运算, 或运算两个值中只要有一个True就会返回True
nums3 = True or True
nums3 = True or False
print(nums3)

# 非布尔值的与或运算
# 与运算, 如果第一个值是False则直接返回第一个值, 否则返回第二个值
nums4 = 1 and 2
nums4 = 1 and 0
nums4 = 0 and 1
nums4 = 0 and None
print(nums4)

# 或运算, 如果第一个值是True则直接返回第一个值, 否则返回第二个值
nums5 = 1 or 2
nums5 = 1 or 0
nums5 = 0 or 1
nums5 = 0 or None
print(nums5)

# 条件运算符 | Conditional operator
# 语法: 语句一 if 条件表达式 else 语句二
# 执行流程:  条件运算符在执行时会先对条件表达式进行求值判断, 如果判断结果为True则执行语句一并返回执行结果, 如果判断结果为False则执行语句二并返回执行结果
if 20 > 18:
    print('大于等于')
else:
    print('小于等于')

nums6 = 50
nums7 = 60
nums8 = 10
mins = nums6 if (nums6 < nums7 and nums6 < nums8) else (nums7 if nums7 < nums8 else nums8)
print('min=', mins)
