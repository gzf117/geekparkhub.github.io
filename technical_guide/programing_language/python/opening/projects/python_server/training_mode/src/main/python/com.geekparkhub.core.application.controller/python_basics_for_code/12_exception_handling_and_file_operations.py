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
# @Program : 异常处理和文件操作 | Exception Handling and File Operations
# @File : 12_exception_handling_and_file_operations.py
# @Description : Python 基础篇 - 异常处理和文件操作 | Python Basics-Exception Handling and File Operations

# 异常 | extremely
print('Extremely!')
try:
    # 捕获异常 | Catch exception
    print(10 / 0)
except:
    # 处理异常 | Handling exceptions
    print('Handling exceptions')
else:
    print('End')

print('Before the exception')
try:
    print(10 / 0)
# Exception是所有异常类的父类, 所以如果except后跟的是Exception则会捕获到所有的异常
except Exception as e:
    print('Exception Info', e)
finally:
    print('无论是否出现异常, 最终该语句都会执行')
print('After the exception')


# 定义 类 | Definition class
class ExceptionClass(Exception):

    # 定义 加法函数 | Definition Addition function
    def additions(self, num1, num2):
        if num1 < 0 or num2 < 0:
            raise ExceptionClass('Custom exception information')
        res1 = num1 + num2
        return res1


# if __name__ == '__main__':
#     # 创建实例 | Create instance
#     ec = ExceptionClass()
#
#     # 调用函数 | call function
#     res2 = ec.additions(1, -1)
#     print(res2)

# 文件 I/O | File I/O
# 打开文件流 | Open file stream
FILE_PATH = '../resources/row_file/part_metadata_user.txt'
FILE_PATHS = '../resources/row_file/demo.jpg'
# row_data = open(FILE_PATH, encoding='UTF-8')

# 读取文件流 | Read file stream
# contents = row_data.read()
# print('contents=', contents)

# 关闭文件流 | Close file stream
# row_data.close()

# 使用 `with ... as ...` 语法 读取文件
try:
    with open(FILE_PATH, encoding='UTF-8') as row_data:
        contents = row_data.read()
        print('contents=', contents)
except Exception as error:
    print('Error info:', error)

# 自定义读取文件大小 | Custom read file size
try:
    with open(FILE_PATH, encoding='UTF-8') as row_data:
        row_content = ''
        SIZE = 328
        while True:
            content = row_data.read(SIZE)
            if not content:
                print('Read finished\n')
                break
            row_content += content
except Exception as error:
    print('Error info:', error)
finally:
    print('row_content=', row_content)

# 读取文件行内容 | Read file line content
try:
    with open(FILE_PATH, encoding='UTF-8') as row_data:
        readline_content = row_data.readline()
        readlines_content = row_data.readlines()
        for x in row_data:
            print('content=', x)
except Exception as error:
    print('Error info:', error)
finally:
    print('readline_content=', readline_content)
    print('readlines_content=', readlines_content[1])

# 写入文件 | Write to file
'''
'r'     open for reading (default)
'w'    open for writing, truncating the file first
'x'     open for exclusive creation, failing if the file already exists
'a'     open for writing, appending to the end of the file if it exists
'b'     binary mode
't'     text mode (default)
'+'     open for updating (reading and writing)

写入文件 参数 `r` : 表示当前文件为只读模式
写入文件 参数 `+` : 操作符添加功能
写入文件 参数 `w` : 表示写入内容时, 将覆盖当前所有文件内容, 如文件不存在, 则将创建文件并写入内容至文件中
写入文件 参数 `a` : 表示写入内容时, 将追加到当前文件中, 如文件不存在, 则将创建文件并写入内容至文件中
'''
try:
    with open(FILE_PATH, 'a') as row_data:
        # row_data.write('Write to file')
        print(row_data)
except Exception as error:
    print('Error info:', error)
finally:
    print('row_data=', row_data)

# 读取 二进制文件 | Read binary file
'''
'b'     binary mode
't'     text mode (default)
'''
try:
    with open(FILE_PATHS, 'rb') as row_datas:
        # byte_size = 100
        # r = row_datas.read(byte_size)
        # print('Binary File=', r)
        # 写入 二进制文件 | Write binary file
        NEW_FILE_PATH = '../resources/row_file/binary_data.jpg'
        with open(NEW_FILE_PATH, 'wb') as new_binary_data:
            byte_size = 1024 * 100
            new_data = ''
            while True:
                row_res = row_datas.read(byte_size)
                if not row_res:
                    print('Read finished\n')
                    break
                new_binary_data.write(row_res)
                new_data += new_binary_data
except Exception as error:
    print('Error info:', error)
finally:
    print('new_data=', new_data)

# 修改 & 查询 读取位置 | Modify & Inquire Read Location
try:
    with open(FILE_PATH, 'rb') as row_data:
        SIZE = 328
        '''
        seek方法 参数说明
        参数 一: 切换读取位置
        参数 二: 计算位置方式 默认值0 从首部计算, 1 从当前位置计算 , 2 从末尾位置开始计算
        '''
        seek_data = row_data.seek(328)
        tell_data = row_data.tell()
        print('Read position -->', tell_data)
        print(row_data.read(SIZE))
except Exception as error:
    print('Error info:', error)

# 文件其他操作 | File other operations
# `os模块` 可以让开发者对操作系统进行访问
import os
from pprint import pprint

# 创建目录 | Create a directory
mk = os.mkdir('../resources/row_file/test_dir')

# 删除目录 | Delete directory
# rm = os.rmdir('../resources/row_file/test_dir')

# 查看当前或指定文件列表 | View a list of current or specified files
dir = os.listdir('.')
pprint(dir)

# 切换目录 | Change directory
cd_dir = os.chdir('..')
pprint(cd_dir)

# 查看当前文件目录 | View the current file directory
pwd = os.getcwd()
pprint(pwd)

# 文件重命名和移动文件 | File renaming And moving files
# os.rename('xxx', 'yyy')

# 删除文件 | Delete Files
os.remove(NEW_FILE_PATH)
