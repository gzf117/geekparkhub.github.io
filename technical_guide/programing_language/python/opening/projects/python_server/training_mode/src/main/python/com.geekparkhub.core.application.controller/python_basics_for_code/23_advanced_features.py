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
# @Program : 高级特性 | Advanced features
# @File : 23_advanced_features.py
# @Description : Python 进阶篇 - 高级特性 | Advanced Python - Advanced Features


# 定义 切片 类 | Definition slice class
class Slice:

    # 定义 获取列表元素 方法 | Definition get list element method
    @staticmethod
    def get_element():
        # 定义 列表 | Definition list
        elements = ['System', 'Karlh', 'Oracy', 'Pob', 'Tack']
        '''
        获取列表前3个元素 切片说明:
        `elements[0:3]` 表示 从索引0开始获取, 直到索引3为止, 但不包括索引3, 即索引 `0, 1, 2`
        '''
        print('=============================== Slice Start ===============================\n')
        print('elements[0:3] =', elements[0:3])

        '''
        获取列表前3个元素 切片说明:
        `elements[:3]` 表示 从索引0开始获取, 如果第一个索引是0, 还可以省略, 直到索引3为止, 但不包括索引3, 即索引 `0, 1, 2`
        '''
        print('elements[:3] =', elements[:3])

        '''
        从索引1开始获取出2个元素 切片说明:
        `elements[1:3]` 表示 从索引1开始获取, 直到索引3为止, 但不包括索引3, 即索引 `1, 2`
        '''
        print('elements[1:3] =', elements[1:3])

        '''
        倒数 切片说明: 
        Python支持`List[-1]`获取 倒数元素, 倒数第一个元素索引是`-1`
        `elements[-2:]` 表示 从元素末尾-1开始获取, 直到索引-2为止, 包括索引-2, 即索引 `-1, -2`
        '''
        print('elements[-2:] =', elements[-2:])

        # 定义 数列 | Definition Number List
        number_elements = list(range(100))
        print('number_elements = ', number_elements)

        '''
        获取列表前10个元素 切片说明:
        `elements[0:10]` 或 `elements[:10]` 表示 从索引0开始获取, 如果第一个索引是0, 还可以省略,
        直到索引10为止, 但不包括索引10, 即索引 `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`
        '''
        print('number_elements[0:10] = ', number_elements[0:10])
        print('number_elements[:10] = ', number_elements[:10])

        '''
        获取列表后10个元素 切片说明:
        `elements[-10:]` 表示 从元素末尾-1开始获取, 直到索引-10为止, 包括索引-10, 即索引 `90, 91, 92, 93, 94, 95, 96, 97, 98, 99`
        '''
        print('number_elements[-10:] = ', number_elements[-10:])

        '''
        获取列表前11~20元素个数 切片说明:
        `number_elements[10:20]` 表示 从元素索引11开始获取, 直到索引20为止, 不包括索引20, 即索引 `10, 11, 12, 13, 14, 15, 16, 17, 18, 19`
        '''
        print('number_elements[10:20] = ', number_elements[10:20])

        '''
        获取列表前10个元素, 每2个元素取1个元素 切片说明:
        `number_elements[0:10:2]` 或 `number_elements[:10:2]` 表示 从索引0开始获取, 如果第一个索引是0, 还可以省略,
        直到索引10为止, 但不包括索引10, 且每两个元素取一个元素, 即索引 `0, 2, 4, 6, 8`
        '''
        print('number_elements[0:10:2] = ', number_elements[0:10:2])
        print('number_elements[:10:2] = ', number_elements[:10:2])

        '''
        获取列表所有元素, 每5个元素取1个元素 切片说明:
        `number_elements[0:100:5]` 或 `number_elements[::5]` 表示 从索引0开始获取, 直到索引10为止, 
        且每5个元素取1个元素, , 即索引 `0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95`
        '''
        print('number_elements[0:100:5] = ', number_elements[0:100:5])
        print('number_elements[::5] = ', number_elements[::5])
        print('\n=============================== Slice End ===============================')

    # 定义 字符串 格式化 方法 | Definition string formatting method
    @staticmethod
    def string_formatting():
        string = '      Hello World !~      '
        if string == ' ' or string.isspace():
            string = ' '
        else:
            while string[0] == ' ':
                string = string[1:]
            while string[-1] == ' ':
                string = string[:-1]
        return print('String Formatting =', string)


# 导入模块 | Import module
from collections import Iterable as ie, Iterator as it


# 定义 迭代 类 | Define iteration class
class iterations:
    # 定义 迭代 静态方法 | Define iterative static method
    @staticmethod
    def iterative():
        print('\n=============================== iterative Start ===============================\n')
        print('Iterable ? [1, 2, 3]:', isinstance([1, 2, 3], ie))
        print('Iterator ? [1, 2, 3]:', isinstance([1, 2, 3], it))

        print('Iterable ? \'abc\':', isinstance('abc', ie))
        print('Iterator ? \'abc\':', isinstance('abc', it))

        print('Iterable ? 123:', isinstance(123, ie))
        print('Iterator ? 123:', isinstance(123, it))

        print('for x in [1, 2, 3, 4, 5]:')
        for x in [1, 2, 3, 4, 5]:
            print('iter List =', x)

        print('for x in iter([1, 2, 3, 4, 5]):')
        for x in iter([1, 2, 3, 4, 5]):
            print('iter List =', x)

        print('next():')
        its = iter([1, 2, 3, 4, 5])
        print('next(its) =', next(its))

        # iter both key and value:
        d = {'a': 1, 'b': 2, 'c': 3}
        print('iter item = ', d)
        for k, v in d.items():
            print('item = ', k, v)

        # iter list with index:
        print('iter enumerate([\'A\', \'B\', \'C\']')
        for iters, value in enumerate(['A', 'B', 'C']):
            print('iter enumerate = ', iters, value)

        # iter complex list:
        print('iter [(1, 1), (2, 4), (3, 9)]:')
        for x, y in [(1, 1), (2, 4), (3, 9)]:
            print('iter = ', x, y)
        print('\n=============================== iterative End ===============================')


# 定义 列表生成式 类 | Definition list generation class
class ListGeneration:
    # 定义 列表生成式 静态方法 | Definition list-generating static method
    @staticmethod
    def list_generating():
        print('\n=============================== List Generation Start ===============================\n')
        print('[x * x for x in range(1, 11)] =', [x * x for x in range(1, 11)])
        print('[x * x for x in range(1, 11) if x % 2 == 0] = ', [x * x for x in range(1, 11) if x % 2 == 0])
        print("[m + n for m in 'ABC' for n in 'XYZ'] = ", [m + n for m in 'ABC' for n in 'XYZ'])

        d = {'x': 'A', 'y': 'B', 'z': 'C'}
        print([k + '=' + v for k, v in d.items()])

        lis = ['Hello', 'World', 'IBM', 'Apple']
        print([strings.lower() for strings in lis])
        print('\n=============================== List Generation End ===============================')


# 定义 生成器 类 | Definition generator class
class Generators:

    # 定义 斐波拉契数列 静态方法 | Definition Fibonacci sequence static method
    @staticmethod
    def fibonacci(max_num):
        n, a, b = 0, 0, 1
        while n < max_num:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'Done'

    # 定义 生成器 方法 | Definition generator method
    def generators(self):
        print('\n=============================== Generator Start ===============================\n')

        string = (x * x for x in range(5))
        print('Returns a Generator Object =', string)
        for x in string:
            print('element =', x)

        # 调用 斐波拉契 | Call Fibonacci
        f = self.fibonacci(10)
        print('\n`fibonacci(10)` Returns a Generator Object =', f)
        for x in f:
            print('fibonacci =', x)
        print('\n')

        # 调用 生成器 | Call generator
        gen = self.fibonacci(5)
        while 1:
            try:
                x = next(gen)
                print('generator =', x)
            except StopIteration as e:
                print('Generator return value =', e.value)
                break
        print('\n=============================== Generators End ===============================')


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 创建对象实例 | Create object instance
    s = Slice()
    i = iterations()
    l = ListGeneration()
    g = Generators()
    # 对象 调用方法 | Object call method
    s.get_element()
    s.string_formatting()
    i.iterative()
    l.list_generating()
    g.generators()
