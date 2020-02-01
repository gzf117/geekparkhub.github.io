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
# @Program : 内建模块 & 第三方模块 | Built-in modules & third-party modules
# @File : 24_built_in_module.py
# @Description : Python 进阶篇 - 内建模块 & 第三方模块 | Advanced Python - Built-in Modules & Third-Party Modules

# 导入模块 | Import module
from datetime import datetime as dt, timedelta as td, timezone as tz
from collections import namedtuple as nt, deque as dq, defaultdict as dd, OrderedDict as odd, Counter as cr


# 定义 内建模块 类 | Definition built-in module class
class BuiltInModule:
    # 定义 日期时间 静态方法 | Definition datetime static method
    @staticmethod
    def datetime_method():
        print('\n=============================== DateTime Method Start ===============================\n')
        # 获取当前日期时间 | Get the current date and time
        now = dt.now()
        print('Now DateTime =', now, '| Type(now) =', type(now))

        # 获取指定日期和时间 | Get the specified date and time
        dts = dt(2019, 8, 19, 23, 00)
        print('DateTime =', dts)

        # 日期时间转换为时间戳 | Datetime to timestamp
        '''
        `timestamp`说明：
                    在计算机中时间实际上是用数字表示, 把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为EpochTime, 记为0
                    (1970年以前的时间timestamp为负数), 当前时间就是相对于EpochTime的秒数, 称为timestamp(时间戳).
                    可见timestamp的值与时区毫无关系, 因为timestamp一旦确定, 其UTC时间就确定了, 
                    转换到任意时区的时间也是完全确定的, 这就是为什么计算机存储的当前时间是以timestamp表示的，
                    因为全球各地的计算机在任意时刻的timestamp都是完全相同的(假定时间已校准)
        '''
        print('DateTime -> TimeStamp =', dt.now().timestamp())

        # 时间戳转换为日期时间 | Timestamp to datetime
        '''
        注意到timestamp是一个浮点数, 它没有时区的概念, 而datetime是有时区, 转换是指在timestamp和本地时间做转换
        本地时间是指当前操作系统设定的时区, 例如北京时区是东8区: `2019-02-01 04:20:10`, 实际上就是UTC+8:00时区的时间: `2019-02-01 04:20:10 UTC+8:00`,
        而此刻的格林威治标准时间与北京时间差了8小时, 也就是UTC+0:00时区的时间应该是：`2019-02-01 04:20:10 UTC+0:00`
        '''
        new_now = dt.now().timestamp()
        print('TimeStamp -> DateTime =', dt.fromtimestamp(new_now))  # 转换为本地时间
        print('TimeStamp -> DateTime as UTC+0 =', dt.utcfromtimestamp(new_now))  # 转换为UTC标准时区时间

        # 字符串转换为日期时间 | String to datetime
        string_datetime = dt.strptime('2019-02-01 04:20:10', '%Y-%m-%d %H:%M:%S')
        print('StringDateTime -> DateTime =', string_datetime)

        # 日期时间转换为字符串 | datetime to String
        print('DateTime -> StringDateTime =', now.strftime('%a, %b %d %H:%M'))

        # 日期时间 加减运算 | Date and time addition and subtraction
        '''
        对日期和时间进行加减实际上就是把datetime往后或往前计算得到新的datetime, 加减可以直接用+和-运算符
        '''
        print('Current DateTime =', string_datetime)
        print('Current + 10 Hours =', string_datetime + td(hours=10))
        print('Current - 1 Day =', string_datetime - td(days=1))
        print('Current + 2.5 Days =', string_datetime + td(days=2, hours=12))

        # 本地时间转换为UTC时间 | Local time to UTC time
        '''
        本地时间是指系统设定时区的时间, 例如北京时间是UTC+8:00时区的时间, 而UTC时间指UTC+0:00时区的时间.
        时区转换的关键在于得到一个datetime时, 需要获知其正确的时区, 然后强制设置时区作为基准时间.
        利用带时区的datetime, 通过astimezone()方法, 可以转换到任意时区.
        '''
        utc_dt = dt.utcnow().replace(tzinfo=tz.utc)  # 设置时区为UTC+0:00
        utc8_dt = utc_dt.astimezone(tz(td(hours=8)))  # 将转换时区为北京时间
        tokyo_dt = utc_dt.astimezone(tz(td(hours=9)))  # 将转换时区为东京时间
        print('UTC+0:00 Now =', utc_dt)
        print('UTC+8:00 Now =', utc8_dt)
        print('UTC+9:00 Now =', tokyo_dt)

        print('\n=============================== DateTime Method End ===============================\n')

    # 定义 集合 静态方法 | Definition collection static method
    @staticmethod
    def collections_method():
        print('\n=============================== Collections Method Start ===============================\n')
        # 元祖 | Tuple
        '''
        函数说明：
        `namedtuple`是一个函数, 它用来创建一个自定义的tuple对象, 并且规定了tuple元素的个数, 并可以用属性而不是索引来引用tuple的某个元素
        使用`namedtuple`可以很方便地定义一种数据类型, 它具备tuple的不变性, 又可以根据属性来引用, 使用十分方便.
        '''
        Point = nt('Point', ['x', 'y'])
        Circle = nt('Circle', ['x', 'y', 'r'])
        p = Point(1, 2)
        c = Circle(1, 2, 10)
        print('Point =', p.x, p.y, isinstance(p, Point), isinstance(p, tuple))
        print('Circle =', c.x, c.y, c.r, isinstance(c, Point), isinstance(c, tuple))

        # deque
        '''
        使用list存储数据时按索引访问元素很快, 但是插入和删除元素就很慢, 因为list是线性存储, 数据量大的时候, 插入和删除效率很低.
        `deque`是为了高效实现插入和删除操作的双向列表, 适合用于队列和栈.
        `deque`除了实现list的`append()`和`pop()`外, 还支持`appendleft()`和`popleft()`, 这样就可以非常高效地往头部添加或删除元素.
        '''
        q = dq(['a', 'b', 'c'])
        q.append('x')
        q.pop()
        q.appendleft('y')
        q.popleft()
        print('deque =', q)

        # defaultdict
        '''
        使用dict时如果引用的Key不存在, 就会抛出KeyError, 如果希望key不存在时返回一个默认值, 就可以用`defaultdict`
        注意默认值是调用函数返回的, 而函数在创建`defaultdict`对象时传入.
        除了在Key不存在时返回默认值, `defaultdict`的其他行为跟dict是完全一样.
        '''
        ddt = dd(lambda: 'N/A')
        ddt['key1'] = 'abc'
        print('ddt[\'key1\'] =', ddt['key1'])
        print('ddt[\'key2\'] =', ddt['key2'])

        # OrderedDict
        '''
        使用dict时Key是无序, 在对dict做迭代时无法确定Key的顺序, 如果要保持Key的顺序可以用`OrderedDict`
        注意OrderedDict的Key会按照插入的顺序排列, 不是Key本身排序.
        '''
        d = dict([('a', 1), ('b', 2), ('c', 3)])
        print('Dict =', d)
        od = odd(d)
        print('OrderedDict =', od)

        od = odd()
        od['z'] = 1
        od['y'] = 2
        od['x'] = 3
        ods = list(od.keys())
        print('OrderedDict =', ods)

        # ChainMap
        '''
        ChainMap可以把一组dict串起来并组成一个逻辑上的dict, 
        ChainMap本身也是一个dict, 但是查找的时会按照顺序在内部的dict依次查找.
        '''

        # Counter | 统计字陆运出现个数
        character = 'https://www.geekparkhub.com'
        c = cr()
        # Statistics Type 1
        c.update(character)
        print('Character Counter =', c)
        # Statistics Type 2
        for ch in character:
            c[ch] = c[ch] + 1
        print('Character Counter =', c)

        print('\n=============================== Collections Method End ===============================\n')


# 导入模块 | Import module

# 定义 第三方模块 类 | Defining third-party module classes
class ThirdPartyModule:
    pass


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 创建 对象实例 | Create object instance
    b = BuiltInModule()
    t = ThirdPartyModule()
    # 对象实例 调用方法 | Object instance call method
    b.datetime_method()
    b.collections_method()
