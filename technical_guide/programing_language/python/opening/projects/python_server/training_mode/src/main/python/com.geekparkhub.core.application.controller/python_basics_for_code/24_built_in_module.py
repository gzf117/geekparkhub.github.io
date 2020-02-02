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
import base64 as b64
import struct as st
import hashlib as hl
import hmac as hm
import itertools as its
from urllib import request as req, parse as pe


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

    # 定义 base64 静态方法 | Defining a base64 static method
    @staticmethod
    def base64_method():
        print('\n=============================== Base64 Method Start ===============================\n')
        # Base64 编码 | Base64 encoding
        base64_encoding = b64.b64encode('BASE64 编码'.encode('UTF-8'))
        print('Base64 encoding =', base64_encoding)
        # Base64 解码 | Base64 decoding
        base64_decoding = b64.b64decode(base64_encoding).decode('UTF-8')
        print('Base64 decoding =', base64_decoding)

        '''
        由于标准的Base64编码后可能出现字符+和/, 在URL中就不能直接作为参数, 
        所以又有一种"url safe"的base64编码,  其实就是把字符+和/分别变成-和_
        '''
        # Base64 编码 for Url Safe | Base64 encoding for Url Safe
        base64_encoding_for_urlsafe_1 = b64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
        base64_encoding_for_urlsafe_2 = b64.urlsafe_b64encode('Base64 encoding for Url Safe'.encode('UTF-8'))
        print('Base64 encoding for Url Safe 1 =', base64_encoding_for_urlsafe_1)
        print('Base64 encoding for Url Safe 2 =', base64_encoding_for_urlsafe_2)

        # Base64 解码 for Url Safe | Base64 decoding for Url Safe
        base64_decoding_for_urlsafe_1 = b64.urlsafe_b64decode(base64_encoding_for_urlsafe_1)
        base64_decoding_for_urlsafe_2 = b64.urlsafe_b64decode(base64_encoding_for_urlsafe_2).decode('UTF-8')
        print('Base64 decoding for Url Safe 1 =', base64_decoding_for_urlsafe_1)
        print('Base64 decoding for Url Safe 2 =', base64_decoding_for_urlsafe_2)

        print('\n=============================== Base64 Method End ===============================\n')

    # 定义 结构 静态方法 | Definition structure static method
    @staticmethod
    def struct_method():
        print('\n=============================== Struct Method Start ===============================\n')
        # 将任意数据类型转换为字节类型 | Convert any data type to byte type
        '''
        struct中pack函数把任意数据类型变成bytes, `pack`的第一个参数是处理指令
        `>I`参数说明：`>` 表示字节顺序是big-endian, 也就是网络序, `I`表示4字节无符号整数, 后面的参数个数要和处理指令一致.
        根据`>IH`的说明, 后面的bytes依次变为 `I`为4字节无符号整数 `H`为2字节无符号整数.
        '''
        # 包装为字节类型 | Packed as a byte type
        packing_byte_type = st.pack('>I', 10240099)
        print('Packing ByteType (`10240099`)=', packing_byte_type)

        # 解包为数据类型 | Unpacked as a data type
        unpacking_data_type = st.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
        print("Unpacking DataType =", unpacking_data_type)

        '''
        BMP 说明：
        bmp是Windows操作系统中一种非常简单位图的文件格式.
        BMP格式采用小端方式存储数据, 文件头的结构按顺序如下
        
        BMP结构按顺序 说明：
        两个字节：`BM`表示Windows位图, `BA`表示OS/2位图. | 一个4字节整数：表示位图大小
        一个4字节整数：保留位, 始终为0 | 一个4字节整数：实际图像的偏移量
        一个4字节整数：Header的字节数 | 一个4字节整数：图像宽度
        一个4字节整数：图像高度 | 一个2字节整数：始终为1 | 一个2字节整数：颜色数
        '''
        bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68' \
                     b'\x01\x00\x00\x01\x00\x18\x00'
        unpacking_bmp = st.unpack('<ccIIIIIIHH', bmp_header)
        print('BMP All Info =', unpacking_bmp)
        print('BMP Type Info =', unpacking_bmp[0], unpacking_bmp[1])
        print('BMP Size Info =', unpacking_bmp[2])
        print('BMP Reserved bit Info =', unpacking_bmp[3])
        print('BMP Offset Info =', unpacking_bmp[4])
        print('BMP Header bytes Info =', unpacking_bmp[5])
        print('BMP width * height Info = ', unpacking_bmp[6], '*', unpacking_bmp[7])
        print('BMP Number of colors Info =', unpacking_bmp[9])
        print('\n=============================== Struct Method End ===============================\n')

    # 定义 摘要 静态方法 | Definition summary static method
    @staticmethod
    def summary_method():
        print('\n=============================== Summary Method Start ===============================\n')
        # 定义 MD5 摘要算法 | Define MD5 Digest Algorithm
        '''
        MD5是最常见的摘要算法, 速度很快, 生成结果是固定的128 bit字节, 通常用一个32位的16进制字符串表示.
        '''
        md5 = hl.md5()
        md5.update('Open Source Open Achievement Dream, GeekParkHub Co-construction has never been seen before.'.encode(
            'UTF-8'))
        md5.update('In the spirit of fearless exploration, create unknown technology and worship of technology.'.encode(
            'UTF-8'))
        md5.update('Advanced Python - Built-in Modules & Third-Party Modules'.encode('UTF-8'))
        print('MD5 Digest Algorithm =', md5.hexdigest())

        # 定义 SHA1 摘要算法 | Define the SHA1 digest algorithm
        '''
        SHA1的结果是160 bit字节, 通常用一个40位的16进制字符串表示.
        '''
        sha1 = hl.sha1()
        sha1.update(
            'Open Source Open Achievement Dream, GeekParkHub Co-construction has never been seen before.'.encode(
                'UTF-8'))
        sha1.update(
            'In the spirit of fearless exploration, create unknown technology and worship of technology.'.encode(
                'UTF-8'))
        sha1.update('Advanced Python - Built-in Modules & Third-Party Modules'.encode('UTF-8'))
        print('SHA1 Digest Algorithm =', sha1.hexdigest())
        print('\n=============================== Summary Method End ===============================\n')

    # 定义 hmac 静态方法 | Define hmac static method
    @staticmethod
    def hmac_method():
        print('\n=============================== HMAC Method Start ===============================\n')
        message = b'Hello, World!'  # 定义 原始消息 | Definition Original Message
        key = b'secret'  # 定义 随机Key | Definition Random Key
        h = hm.new(key, message, digestmod='MD5')
        print('HMAC Digest Algorithm =', h.hexdigest())
        print('\n=============================== HMAC Method End ===============================\n')

    # 定义 itertools 静态方法 | Define itertools static method
    @staticmethod
    def itertools_method():
        print('\n=============================== itertools Method Start ===============================\n')
        # count()
        '''
        count() 将创建一个无限的迭代器, 所以代码会打印出自然数序列无法自动退出, 只能按Ctrl+C退出
        '''
        natuals = its.count(1)
        for x in natuals:
            print('natuals =', x)
            if x >= 10:
                break

        # cycle()
        '''
        cycle() 将传入的序列无限重复循环
        '''
        cs = its.cycle('ABC')
        frequency = 10
        for c in cs:
            print('Infinite repeat loop Frequency = %d Values = %s ' % (frequency, c))
            frequency = frequency - 1
            if frequency == 0:
                break

        # repeat()
        '''
        repeat()负责把一个元素无限重复循环, 不过如果提供第二个参数就可以限定重复次数
        '''
        ns = its.repeat('A', 3)
        for n in ns:
            print('Limited number of repetitions =', n)

        # takewhile()
        '''
        无限序列只有在for迭代时才会无限地迭代下去, 如果只是创建了一个迭代对象,
        它不会事先把无限个元素生成出来, 事实上也不可能在内存中创建无限多个元素.
        无限序列虽然可以无限迭代下去, 但是通常会通过`takewhile()`等函数根据条件判断来截取出一个有限的序列.
        '''
        natuals = its.count(1)
        tw = its.takewhile(lambda x: x <= 10, natuals)
        print('natuals =', list(tw))

        # chain()
        '''
        chain() 将一组迭代对象串联起来形成一个更大的迭代器
        '''
        for cn in its.chain('ABC', 'XYZ'):
            print('Tandem Iterator =', cn)

        # groupby()
        '''
        groupby() 将迭代器中相邻的重复元素挑出来放在一起
        '''
        for key1, group1 in its.groupby('AAABBBCCAAA'):
            print(f'Key_1 = {key1}', list(group1))

        for key2, group2 in its.groupby('AaaBBbcCAAa', lambda cc: cc.upper()):
            print(f'Key_2 = {key2}', list(group2))
        print('\n=============================== itertools Method End ===============================\n')

    # 定义 请求 静态方法 | Definition request static method
    @staticmethod
    def request_library_method():
        print('\n=============================== Request Method Start ===============================\n')
        # 定义 Get请求 | Define Get Request
        reqs = req.Request('http://www.baidu.com')
        reqs.add_header('User-Agent',
                        'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        with req.urlopen(reqs) as f:
            data = f.read()
            print('Status =>', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data =>\n', data.decode('UTF-8'))

        # 定义 Post请求 | Define Post Request
        print('Login to weibo.cn...')
        email = 'xxx@xxx.org'
        passwd = 'xxxxx'
        login_data = pe.urlencode([
            ('username', email),
            ('password', passwd),
            ('entry', 'mweibo'),
            ('client_id', ''),
            ('savestate', '1'),
            ('ec', ''),
            ('pagerefer',
             'http://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom&jumpfrom=weibocom')
        ])
        login_req = req.Request('http://passport.weibo.cn/sso/login')
        login_req.add_header('Origin', 'http://passport.weibo.cn')
        login_req.add_header('User-Agent',
                             'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        login_req.add_header('Referer',
                             'http://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom')
        with req.urlopen(login_req, data=login_data.encode('utf-8')) as func:
            print('Status:', func.status, func.reason)
            for keys, values in func.getheaders():
                print('%s: %s' % (keys, values))
            print('Data:', func.read().decode('UTF-8'))

        # 定义 代理身份验证 | Define proxy authentication
        proxy_handler = req.ProxyHandler({'http': 'http://www.example.com:3128/'})
        proxy_auth_handler = req.ProxyBasicAuthHandler()
        proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
        opener = req.build_opener(proxy_handler, proxy_auth_handler)
        with opener.open('http://www.example.com/login.html') as fn:
            pass

        print('\n=============================== Request Method End ===============================\n')


# 导入模块 | Import module
from contextlib import contextmanager as cm
from contextlib import closing as cg


# from urllib.request import urlopen as uo


# 定义 上下文库 | Definition context library
class BuiltInModuleForContextLibrary(object):
    # 定义 初始化 方法 | Define initialization method
    def __init__(self, name):
        self.name = name

    # 自定义 方法 | Custom method
    def query(self):
        print('Query info about %s...' % self.name)


'''
`@contextmanager`这个decorator接受一个generator, 用yield语句把`with ... as var`把变量输出, 然后with语句就可以正常执行
代码执行顺序 说明：
1.with语句首先执行yield之前的语句,因此打印出<h1>
2.yield调用会执行with语句内部的所有语句, 因此打印出Hello和World
3.最后执行yield之后的语句打印出</h1>
因此`@contextmanager`通过编写generator来简化上下文管理
'''


@cm
def create_query(name):
    print('Begin')
    q = BuiltInModuleForContextLibrary(name)
    yield q
    print('End')


# `@contextmanager`实现在某段代码执行前后自动执行特定代码
@cm
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("Hello")
    print("World")

'''
如果一个对象没有实现上下文就不能把它用于with语句, 这个时候可以用closing()来把该对象变为上下文对象, 
例如用with语句使用urlopen(), closing也是一个经过`@contextmanager`装饰的generator, 作用就是把任意对象变为上下文对象并支持with语句
'''
with cg(req.urlopen('http://www.baidu.com')) as page:
    for line in page:
        print('line =', line)


@cm
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


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
    b.base64_method()
    b.struct_method()
    b.summary_method()
    b.hmac_method()
    b.itertools_method()
    b.request_library_method()
    # 调用 函数 | call function
    create_query('1')
    closing('2')
