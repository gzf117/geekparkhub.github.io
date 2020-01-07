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


# 定义函数 | Defining functions
def functions8():
    return 100


# 调用函数 | call function
r = functions8()
print('r=', r)


# 定义函数 | Defining functions
def functions9(*nums):
    res = 0  # 定义初始化变量, 保存结果集
    for data in nums:
        res += data
        return res


# 调用函数 | call function
r1 = functions9(10)
print('r1=', r1 + 10)

# 调用help函数
help(print)  # 查询print函数使用方法
help(dict)  # 查询dict函数使用方法
help(map)  # 查询map函数使用方法


def functions10(value1: int, value2: bool, value3: str = 'string') -> int:
    '''
    自定义函数 实例

    自定义函数 作用：

    自定义函数 参数：
        `value1` 作用 / 类型 / 默认值 .....
        `value2` 作用 / 类型 / 默认值 .....
        `value3` 作用 / 类型 / 默认值 .....
    '''
    print('functions10')


help(functions10)  # 查询自定义函数使用方法

# 作用域 | Scope
# 定义变量 用于全局作用域 | Define variables for global scope
variables = 10


# 定义函数 | Defining functions
def functions11():
    '''
    定义变量 用于局部作用域 | Define variables for local scope
    `data2`变量定义在函数内部,所以它的作用域就是在函数内部,函数外部无法访问
    :return:
    '''
    data2 = 10
    global data1  # 声明`data1`在函数内部变量为全局变量
    data1 = 10

    print('函数内部声明全局变量=', data1)
    print('函数内部=', data2)


print('函数外部=', variables)

# 调用函数 | call function
functions11()

# 命名空间 | Namespaces
'''
`locals()`函数用来获取当前作用域的命名空间, 返回值类型是字典类型
如果在全局作用域中调用此函数则是获取全局命名空间
如果在函数作用域中调用次函数则是获取函数命名空间
'''
namespaces = locals()
print('Namespaces=', namespaces, '\ntype=', type(namespaces))


# 定义函数 | Defining functions
def functions12():
    '''
    `globals()`函数可以用来在任意位置获取全局命名空间
    '''
    namespaces1 = globals()
    print('Namespaces=', namespaces1, '\ntype=', type(namespaces1))


# 调用函数 | call function
functions12()


# 递归 | Recursive
# 无穷递归: 如果此函数被调用时,容易导致程序内存溢出,效果类似于死循环
def functions13():
    functions13()


# 定义 递归函数 | Defining Recursive functions
# 求任意数字的阶乘 | Find the factorial of any number
def functions14(num: int) -> int:
    # 定义 基线条件: 判断num是否等于1, 如果等于1则不再进行递归调用
    if num == 1:
        return 1
    else:
        # 定义 递归条件：如果num=10则返回num*自身函数(num-1)的阶乘 => 10 * 9!
        return num * functions14(num - 1)


# 求任意数字的幂次方 | Find the power of any number
def functions15(num1, num2):
    # 定义 基线条件: 求1幂运算
    if num2 == 1:
        return num1
    else:
        # 定义 递归条件
        return num1 * functions15(num1, num2 - 1)


# 定义 检查回文 函数 | Definition check palindrome function
def check_palindrome(string):
    # 定义 基线条件
    if len(string) < 2:
        return True
    elif string[0] != string[-1]:
        return False
    # 定义 递归条件
    return check_palindrome(string[1: 1])


# 调用函数 | call function
print('functions14=', functions14(10))
print('functions15=', functions15(8, 6))
print('check_palindrome=', check_palindrome('abccba'))
print('check_palindrome=', check_palindrome('abc'))
print('check_palindrome=', check_palindrome('123'))
print('check_palindrome=', check_palindrome('123321'))

# 高阶函数 | higherOrderFunctions
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 定义函数 | Defining functions
def higher_order_function(data):
    # 定义 检查奇数函数
    def odd_function(num):
        if num % 2 == 0:
            return True
        return False

    # 定义 检查 列表中大于6的数值函数
    def more_than_the(num):
        if num > 6:
            return True
        return False

    new_list = []  # 定义 空集合, 用于储存奇数集合
    for x in data:
        if odd_function(x):
            new_list.append(x)
        if more_than_the(x):
            new_list.append(x)
    return new_list


# 调用函数 | call function
print('higher_order_function=', higher_order_function(list_1))
