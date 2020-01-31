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


# 定义 主模块 | Definition Main module
if __name__ == '__main__':
    # 创建对象实例 | Create object instance
    s = Slice()
    # 对象 调用方法 | Object call method
    s.get_element()
    s.string_formatting()
