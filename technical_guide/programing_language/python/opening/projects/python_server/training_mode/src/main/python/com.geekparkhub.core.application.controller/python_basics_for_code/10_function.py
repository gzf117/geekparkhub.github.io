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


# 定义 检查偶数数函数 | Definition check even function
def even_function(num):
    if num % 2 == 0:
        return True
    return False


# 定义 检查奇数函数 | Definition check odd function
def odd_function(num):
    if num % 3 == 0:
        return True
    return False


# 定义 检查 列表中大于6的数值函数
def more_than_the(num):
    if num > 6:
        return True
    return False


# 定义函数 | Defining functions
def higher_order_function(functions, data):
    new_list = []  # 定义 空集合, 用于储存奇数集合
    for x in data:
        if functions(x):
            new_list.append(x)
    return new_list


# 调用函数 | call function
print('higher_order_function=', higher_order_function(even_function, list_1))
print('higher_order_function=', list(filter(odd_function, list_1)))
print('higher_order_function=', list(filter(more_than_the, list_1)))

# 匿名函数 | Anonymous function
anonymous_function01 = (lambda a, b: a * b)
anonymous_function02 = (lambda a, b: a + b)(30, 30)
anonymous_function03 = (lambda x: x % 2 == 0)
anonymous_function04 = (lambda x: x % 2 != 0)
anonymous_function05 = (lambda x: x > 5)

print('anonymous_function01=', anonymous_function01)
print('anonymous_function02=', anonymous_function02)
print('anonymous_function03=', list(filter(anonymous_function03, list_1)))
print('anonymous_function04=', list(filter(anonymous_function04, list_1)))
print('anonymous_function05=', list(filter(anonymous_function05, list_1)))

# map函数 | map function
maps1 = map(lambda x: x + 1, list_1)
maps2 = map(lambda x: x ** 2, list_1)
print('maps1=', list(maps1))
print('maps2=', list(maps2))

# sort方法 | sort method
list_2 = ['b', 'a', 'd', 'c']
list_3 = ['bb', 'aaa', 'dddd', 'ccccc']
list_2.sort()
# list_3.sort(key=len)

print('sort=', list_2)
print('sort=', list_3)

# sorted函数 | sorted function
list_4 = [3, '1', 5, '9', 2, '4', 7, 6]
print('Before sorting: ', list_4)
print('Sorted: ', sorted(list_4, key=int))
print('After sorting: ', list_4)

list_5 = 'iighrghcjshfjkewhfiwlkgoaggdljhsjdewkfk'
print('Before sorting: ', list_5)
print('Sorted: ', sorted(list_5, key=str))
print('After sorting: ', list_5)


# 闭包 | Closure
# 定义函数 | Defining functions
def functions16():
    def inner():
        print('inner !')

    # 将内部函数作为返回值 | Using internal functions as return values
    return inner


# 调用函数 | call function
print('functions16=', functions16())
'''
r16是一个函数, 是调用functions16()后返回的函数
此函数是在functions16()内部定义, 并不是全局函数
所以此函数总是能访问到functions16()函数内的变量
'''
r16 = functions16()
r16()


# 定义函数 | Defining functions
def functions17():
    # 定义 内部空集合 | Definition Internal empty collection
    nums = []

    # 定义 内部函数 | Definition internal function
    def functions18(num):
        # 添加集合元素 | Adding collection elements
        nums.append(num)
        # 计算返回平均值 | Calculate return average
        return sum(nums) / len(nums)

    # 将内部函数作为返回值返回 | Return internal function as return value
    return functions18


# 调用函数 | call function
# 在外部无法访问内部空集合, 只有在内部可以访问, 即表示变量的私有属性
functions19 = functions17()
print('functions19=', functions19(30))
print('functions19=', functions19(3020))
print('functions19=', functions19(5020))

# 装饰器 | Decorator
# 定义函数 | Defining functions
'''
当前方式, 已经可以在不修改源代码的情况下对函数进行扩展
但是当前方式要求在每扩展一个函数就要手动创建一个新的函数实在是太麻烦
为了解决这个问题, 则创建一个函数, 让这个函数可以自动的帮助生产函数
'''

#
def functions20(num1, num2):
    print('res=', num1 * num2)


# 定义函数 | Defining functions
def functions21(num1, num2):
    print('Start Calculating...')
    functions20(num1, num2)
    print('End Calculation...')


# 调用函数 | call function
functions21(5, 6)

# 定义函数 | Defining functions
'''
此函数用来对其他函数进行扩展, 使其他函数可以在执行前后打印日志信息
函数参数：`fun` 需要扩展的函数对象
'''


def extension_function(fun):
    '''
    定义 装饰器函数 | Define decorator function

    `decorator_function()`函数就称之为装饰器
    通过装饰器可以在不修改原来函数的情况下来对函数进行扩展
    在开发中都是通过装饰器来扩展函数的功能
    在定义函数时可以通过`@`装饰器来使用指定的装饰器来装饰当前的函数
    可以同时为一个函数指定多个装饰器, 这样函数将会按照从内向外的顺序被装饰

    非必填参数 args
    非必填参数 keywords
    :param fun:
    :return:
    '''

    def decorator_function(*args, **keywords):
        print('Begin execution')
        # 调用被扩展函数 | Call the extended function
        result = fun(*args, **keywords)
        print('End execution')
        # 返回函数执行结果 | Returns the result of function execution
        return result

    # 返回新函数 | Return new function
    return decorator_function


funs = extension_function(functions20)
r18 = funs(10, 20)

# 定义 扩展函数 | Definition extension function
'''
    在定义函数时可以通过`@`装饰器来使用指定的装饰器来装饰当前的函数
    可以同时为一个函数指定多个装饰器, 这样函数将会按照从内向外的顺序被装饰
'''


# 引入 自定义装饰器 | Introducing custom decorators
@extension_function
def hello():
    print('Hello World ~')


# 调用函数 | call function
hello()
