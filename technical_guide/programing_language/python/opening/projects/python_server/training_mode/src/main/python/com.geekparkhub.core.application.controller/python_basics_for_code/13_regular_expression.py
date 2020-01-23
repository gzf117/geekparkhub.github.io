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
# @Program : 正则表达式 | Regular expression
# @File : 13_regular_expression.py
# @Description : Python 进阶篇 - 正则表达式 | Python Advanced articles - Regular Expressions

# 导入模块 | Import module
import re

# match函数 | match function
'''
`match`尝试从字符串的起始位置匹配一个模式
如果不是起始位置匹配成功的话, match()就返回None
函数 语法: `re.match(pattern, string, flags=0)`
'''


# 定义 函数 | Definition function
def fun1():
    # 在起始位置匹配 | Match at starting position
    r1 = re.match('www', 'www.geekparkhub.com').span()
    print(r1)
    # 不在起始位置匹配 | Do not match at the beginning
    r2 = re.match('com', 'www.geekparkhub.com')
    print(r2)


# 定义常量 | Defining constants
data1 = 'Open Source Open Achievement Dream, GeekParkHub Co-construction has never been seen before.'


# 定义 函数 | Definition function
def fun2(values):
    '''
    r3语句说明:
                    `r`表示字符串为非转义的原始字符串, 让编译器忽略反斜杠, 也就是忽略转义字符,
                    但是这个字符串里没有反斜杠, 所以当前`r`可有可无.

    参数说明:
                第一个匹配分组 (.*)，`.*` 代表匹配除换行符之外所有字符
                第一个匹配分组 (.*?), `.*?` 后面多个问号代表非贪婪模式, 也就是说只匹配符合条件的最少字符
                最后 `.*` 没有括号包围, 所以不是分组, 匹配效果和第一组一样, 但是不计入匹配结果中
                `re.M` 表示多行匹配, 影响 ^ 和 $
                `re.I` 表示使匹配对大小写不敏感
    :param values:
    :return:
    '''
    r3 = re.match(r'(.*?) .*? Open (.*) .*', values, re.M | re.I)
    if r3:
        print('r3.group()=', r3.group())  # r3.group() 等同于 r3.group(0), 表示匹配到完整文本字符
        print('r3.group(1)=', r3.group(1))  # r3.group(1) 得到第一组匹配结果, 也就是(.*)匹配到的
        print('r3.group(2)=', r3.group(2))  # r3.group(2) 得到第二组匹配结果, 也就是(.*?)匹配到的
        # print('r3.group(3)=', r3.group(3))  # 因为只有匹配结果中只有两组所以如果分组为3时会报错
    else:
        print('Match failed!')


# search 方法 | search method
'''
`re.search` 扫描整个字符串并返回第一个成功的匹配
函数语法: `re.search(pattern, string, flags=0)`
'''


# 定义 函数 | Definition function
def fun3():
    # 在起始位置匹配 | Match at starting position
    r1 = re.search('www', 'www.geekparkhub.com').span()
    print(r1)
    # 不在起始位置匹配 | Do not match at the beginning
    r2 = re.search('com', 'www.geekparkhub.com').span()
    print(r2)


# 定义 函数 | Definition function
def fun4(values):
    r4 = re.search(r'(.*?) .*? Open (.*) .*', values, re.M | re.I)
    if r4:
        print('r4.group()=', r4.group())
        print('r4.group(1)=', r4.group(1))
        print('r4.group(2)=', r4.group(2))
    else:
        print('Match failed!')


# 检索和替换 | Retrieve and replace
'''
sub用于替换字符串中的匹配项
语法: `re.sub(pattern, repl, string, count=0, flags=0)`
参数: pattern : 正则中的模式字符串
        repl : 替换的字符串, 也可为一个函数
        string : 要被查找替换的原始字符串
        count : 模式匹配后替换的最大次数, 默认 0 表示替换所有的匹配
'''
# 定义常量 | Defining constants
data2 = '123-456-789 # 替换字符串中的匹配项'


# 定义 函数 | Definition function
def fun5(values):
    # 删除`Python注释`字符串
    r5 = re.sub(r'#.*$', "", values)
    # 删除`-`字符串
    r6 = re.sub(r'\D', "", values)
    print('r5=', r5)
    print('r6=', r6)


'''
repl 函数
将字符串中的匹配的数字乘11
'''
# 定义常量 | Defining constants
data3 = 'P45G3GKFC755'


# 定义 函数 | Definition function
def fun6(matched):
    r7 = int(matched.group('value'))
    return str(r7 * 11)


r8 = re.sub('(?P<value>\d+)', fun6, data3)
print('r8=', r8)

# compile 函数 | compile function
'''
`compile`函数用于编译正则表达式, 生成一个正则表达式(Pattern)对象供`match()`&`search()`这两个函数使用
函数语法: `re.compile(pattern[, flags])`
参数说明: `pattern` 一个字符串形式的正则表达式
              `flags`可选项, 表示匹配模式, 比如忽略大小写, 多行模式等, 具体参数为：
                    1. `re.I 忽略大小写` 2. `re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境`
                    3. `re.M 多行模式` 4. `re.S 即为 . 并且包括换行符在内的任意字符 (. 不包括换行符)`
                    5. `re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库`
                    6. `re.X 为了增加可读性, 忽略空格和 # 后面的注释`
'''
# 定义常量 | Defining constants
data4 = 'one12twothree34four'
data5 = 'Hello Python'


# 定义 函数 | Definition function
def fun7(values):
    r9 = re.compile(r'\d+')  # 用于匹配至少一个数字
    r10 = r9.match(values, 3, 10)  # 从'1'的位置开始匹配
    r11 = r10.group(0)
    r12 = r10.start(0)
    r13 = r10.end(0)
    r14 = r10.span(0)
    print('r10=', r10)
    print('group=', r11)
    print('start=', r12)
    print('end=', r13)
    print('span=', r14)


# 定义 函数 | Definition function
def fun8(values):
    r15 = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # `re.I`表示忽略大小写
    r16 = r15.match(values)
    r17 = r16.group(0)  # 返回匹配成功的整个子串
    r18 = r16.group(1)  # 返回第一个分组匹配成功的子串
    r19 = r16.group(2)  # 返回第二个分组匹配成功的子串
    r20 = r16.span(1)  # 返回第一个分组匹配成功的子串的索引
    r21 = r16.span(2)  # 返回第二个分组匹配成功的子串
    r22 = r16.groups(1)  # 等价于 r16.group(1), r16.group(2), ...)
    print('r16=', r16)
    print('r17=', r17)
    print('r18=', r18)
    print('r19=', r19)
    print('r20=', r20)
    print('r20=', r20)
    print('r21=', r21)
    print('r22=', r22)


# findall & finditer & split
'''
`findall` 在字符串中找到正则表达式所匹配的所有子串并返回一个列表, 如果没有找到匹配的则返回空列表
注意: `match` & `search` 是匹配一次, 而`findall`匹配所有
语法: `findall(string[, pos[, endpos]])`
参数说明: 
            `string` 待匹配的字符串
            `pos` 可选参数, 指定字符串的起始位置, 默认为0
            `endpos` 可选参数指定字符串的结束位置, 默认为字符串的长度
            
=================================================================================

`finditer` 和 `findall` 类似, 在字符串中找到正则表达式所匹配的所有子串并把它们作为一个迭代器返回.
语法: `re.finditer(pattern, string, flags=0)`
参数说明: 
            `pattern` 匹配的正则表达式
            `string` 要匹配的字符串
            `flags` 标志位用于控制正则表达式的匹配方式, 如是否区分大小写, 多行匹配等等
            
=================================================================================

`split` 方法按照能够匹配的子串将字符串分割后返回列表
语法: `re.split(pattern, string[, maxsplit=0, flags=0])`
参数说明: 
            `pattern` 匹配的正则表达式
            `string` 要匹配的字符串
            `maxsplit` 分隔次数, `maxsplit=1`分隔一次, 默认为0, 不限制次数
            `flags` 标志位用于控制正则表达式的匹配方式, 如是否区分大小写, 多行匹配等等
'''
# 查找字符串中所有数字
# 定义常量 | Defining constants
data6 = 'd4qw564df56qw456qw4f56q465df4qwef'


# 定义 函数 | Definition function
def fun9(values):
    r23 = re.compile(r'\d+')  # 检索数字
    r24 = r23.findall(values, 0, 33)
    print('r24=', r24)
    r25 = re.finditer(r'\d+', values)
    for x in r25:
        print('r25=', x.group())


# 定义常量 | Defining constants
data7 = 'Java, C, GoLang, Python'


# 定义 函数 | Definition function
def fun10(values):
    r26 = re.split('(\W+)', values, 1)
    print('r26=', r26)


'''
正则表达式对象 | Regular expression object
re.RegexObject: `re.compile() 返回 RegexObject 对象`
re.MatchObject: 
                        `group() 返回被 RE 匹配的字符串`
                        `start() 返回匹配开始的位置`
                        `end() 返回匹配结束的位置`
                        `span() 返回一个元组包含匹配 (开始,结束) 的位置`

'''
# 定义常量 | Defining constants
data8 = '360523198021445754'


# 定义 函数 | Definition function
def fun11(values):
    '''
    参数说明:
                `?` 表示匹配0个或1个由前面的正则表达式定义的片段, 非贪婪方式
                `P` 表示命名分组, 为当前组起别名
                '\d' 表示匹配任意数字等价于 [0-9]
                `{3}` 表示精确匹配n个前面表达式
    语句说明:
                `(?P<Province>\d{3})` 表示匹配前三位数字, 并将该组命名为`Province`
                `(?P<City>\d{3})` 表示表示匹配前三位数字, 并将该组命名为`City`
                `(?P<BornYear>\d{4})` 表示匹配前四位数字, 并将该组命名为`BornYear`
    :param values:
    :return:
    '''
    r27 = re.search('(?P<Province>\d{3})(?P<City>\d{3})(?P<BornYear>\d{4})', values)
    r28 = r27.groupdict()
    print('r28=', r28)


# 正则表达式实例 | Regular expression example
# 匹配 字符类 | Match character class
'''
匹配 "Python" 或 "python" | Matches "Python" or "python"
'''
# 定义常量 | Defining constants
data9 = 'Python'
r29 = re.match(r'[Pp]', data9, re.M | re.I).group()
print('r29=', r29)

'''
匹配 "ruby" 或 "rube" | Matches "ruby" or "rube"
'''
# 定义常量 | Defining constants
data10 = 'rube'
r30 = re.match(r'rub[ye]', data10, re.M | re.I).group()
print('r30=', r30)

'''
匹配中括号内的任意一个字母 | Matches any letter in brackets
'''
# 定义常量 | Defining constants
data11 = 'dswdwdwletters'
r31 = re.search(r'[letter]', data11, re.M | re.I).group()
print('r31=', r31)

'''
匹配任何数字, 类似 [0123456789] | Matches any number, like [0123456789]
'''
# 定义常量 | Defining constants
data12 = '56468547564897748'
r32 = re.search(r'[0-9]', data12, re.M | re.I).group()
print('r32=', r32)

'''
匹配任何小写字母 | Matches any lowercase letter
'''
# 定义常量 | Defining constants
data13 = 'Python'
r33 = re.search(r'([a-z])', data13, re.M).group()
print('r33=', r33)

'''
匹配任何大写字母 | Match any capital letter
'''
# 定义常量 | Defining constants
data14 = 'Ai'
r34 = re.search(r'([A-Z])', data14, re.M).group()
print('r34=', r34)

'''
匹配任何字母及数字 | Match any letter and number
'''
# 定义常量 | Defining constants
data15 = 'rube'

'''
除了index字母以外的所有字符 | All characters except the index letter
'''
# 定义常量 | Defining constants
data16 = 'rube'

'''
匹配除了数字外的字符 | Matches characters other than numbers
'''
# 定义常量 | Defining constants
data17 = 'rube'

# 匹配 特殊字符类 | Match special character class
'''
匹配除 "\n" 之外的任何单个字符, 要匹配包括 '\n'在内的任何字符, 请使用类似 '[.\n]' 模式
'''
# 定义常量 | Defining constants
data18 = 'rube'

'''
匹配一个数字字符, 等价于 [0-9] | Matches a numeric character, equivalent to [0-9]
'''
# 定义常量 | Defining constants
data19 = 'rube'

'''
匹配一个非数字字符。等价于 [^0-9] " | Matches a non-numeric character. Equivalent to [^ 0-9]
'''
# 定义常量 | Defining constants
data20 = 'rube'

'''
匹配任何空白字符, 包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]
'''
# 定义常量 | Defining constants
data21 = 'rube'

'''
匹配任何非空白字符, 等价于 [^ \f\n\r\t\v] | Matches any non-whitespace character, equivalent to [^ \ f \ n \ r \ t \ v]
'''
# 定义常量 | Defining constants
data22 = 'rube'

'''
匹配包括下划线的任何单词字符, 等价于'[A-Za-z0-9_]' | Matches any word character including underscore, equivalent to '[A-Za-z0-9_]'
'''
# 定义常量 | Defining constants
data23 = 'rube'

'''
匹配任何非单词字符, 等价于 '[^A-Za-z0-9_]' | Matches any non-word character, equivalent to '[^ A-Za-z0-9_]'
'''
# 定义常量 | Defining constants
data24 = 'rube'

# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    fun1()
    fun2(data1)
    fun3()
    fun4(data1)
    fun5(data2)
    fun7(data4)
    fun8(data5)
    fun9(data6)
    fun10(data7)
    fun11(data8)
